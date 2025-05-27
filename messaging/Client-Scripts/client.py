"""DOES NOT WORK ATM"""


# to-do:
# chatrooms
# user to user chats
# Terminal UI

# client.py
import threading
import requests
import time
import json

class HttpClient:
    def __init__(self, base_url: str, poll_interval: float = 1.0):
        self.base_url = base_url.rstrip('/')
        self.poll_interval = poll_interval
        self.received_messages = []
        self._stop_event = threading.Event()
        # start polling thread
        self._listener = threading.Thread(target=self._poll_messages, daemon=True)
        self._listener.start()

    def _poll_messages(self):
        while not self._stop_event.is_set():
            try:
                resp = requests.get(f"{self.base_url}/messages")
                if resp.ok:
                    data = resp.json()
                    self.received_messages = data.get('messages', [])
            except Exception:
                pass
            time.sleep(self.poll_interval)

    def send(self, msg: str):
        """
        Send a message to the server via HTTP POST.
        """
        payload = {'message': msg}
        try:
            resp = requests.post(f"{self.base_url}/message", json=payload)
            return resp.ok
        except Exception:
            return False

    def stop(self):
        """
        Stop the polling thread.
        """
        self._stop_event.set()
        self._listener.join()

if __name__ == '__main__':
    # use your Cloudflare tunnel address here
    client = HttpClient('', poll_interval=2.0)
    try:
        while True:
            text = input("Enter message (or 'quit'): ")
            if text.lower() == 'quit':
                break
            success = client.send(text)
            print("Sent" if success else "Failed to send")
            print("Messages:", json.dumps(client.received_messages, indent=2))
    finally:
        client.stop()
        print("Client stopped")
