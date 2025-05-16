import socket
import threading

HOST = '127.0.0.1'
PORT = 65432
connections = []

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    connections.append(conn)
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode('utf-8').strip()
            print(f"Received from {addr}: {message}")
            for client_conn in connections:
                if client_conn != conn:
                    try:
                        client_conn.sendall(f"{addr[0]}:{addr[1]}: {message}".encode('utf-8'))
                    except:
                        connections.remove(client_conn)
            if message.lower() == 'quit':
                break
    finally:
        connections.remove(conn)
        conn.close()
        print(f"Connection closed with {addr}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()