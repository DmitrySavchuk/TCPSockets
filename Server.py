import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)   # socket creation
server_socket.bind(('127.0.0.1', 53210))   # placing
server_socket.listen(100)   # queue of TCP connections

while True:
    client_socket, client_address = server_socket.accept()

    while True:
        data = client_socket.recv(1024)

        if not data:
            break

        client_socket.sendall(data)

    client_socket.close()
