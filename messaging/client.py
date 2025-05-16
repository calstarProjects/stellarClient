import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")

        def receive_messages():
            while True:
                try:
                    data = s.recv(1024)
                    if not data:
                        break
                    print(data.decode('utf-8'))
                except ConnectionResetError:
                    print("Connection to server closed.")
                    break
                except Exception as e:
                    print(f"Error receiving message: {e}")
                    break

        receive_thread = threading.Thread(target=receive_messages)
        receive_thread.start()

        while True:
            message = input()
            if message.lower() == 'quit':
                break
            s.sendall(message.encode('utf-8'))

    except ConnectionRefusedError:
        print("Connection to server refused. Make sure the server is running.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 's' in locals() and s:
            s.close()