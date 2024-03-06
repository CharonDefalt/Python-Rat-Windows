import socket

HOST = '192.168.121.105'  # Change this to the IP address of the server
PORT = 85         # Port on which the server is listening

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("[*] Connected to server.")

while True:
    command = input("Enter command ('exit' to quit): ")
    client_socket.send(command.encode())
    if command.lower() == 'exit':
        break
    response = client_socket.recv(4096).decode()
    print(response)

client_socket.close()
