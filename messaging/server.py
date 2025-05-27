"""DOES NOT WORK ATM"""

# server.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import json

HOST = ''  # Replace with your server's hostname or IP
PORT = 8080

class ThreadedHTTPServer(HTTPServer, threading.Thread):
    """Handle requests in separate threads."""
    allow_reuse_address = True

class RequestHandler(BaseHTTPRequestHandler):
    # shared, thread-safe list of messages
    messages = []
    lock = threading.Lock()

    def _set_headers(self, status=200, content_type='application/json'):
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.end_headers()

    def do_POST(self):
        # Endpoint to receive a message
        if self.path == '/message':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            try:
                data = json.loads(body)
                msg = data.get('message', '')
                addr = self.client_address
                with RequestHandler.lock:
                    RequestHandler.messages.append({'from': addr, 'message': msg})
                print(f"Received from {addr}: {msg}")
                self._set_headers()
                self.wfile.write(json.dumps({'status': 'ok'}).encode('utf-8'))
            except json.JSONDecodeError:
                self._set_headers(400)
                self.wfile.write(json.dumps({'error': 'Invalid JSON'}).encode('utf-8'))
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({'error': 'Not found'}).encode('utf-8'))

    def do_GET(self):
        # Endpoint to fetch all messages
        if self.path == '/messages':
            with RequestHandler.lock:
                msgs = list(RequestHandler.messages)
            self._set_headers()
            self.wfile.write(json.dumps({'messages': msgs}).encode('utf-8'))
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({'error': 'Not found'}).encode('utf-8'))

    def log_message(self, format, *args):
        # suppress default logging
        return

if __name__ == '__main__':
    server = ThreadedHTTPServer((HOST, PORT), RequestHandler)
    print(f"HTTP server running on http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        print("Server stopped")
