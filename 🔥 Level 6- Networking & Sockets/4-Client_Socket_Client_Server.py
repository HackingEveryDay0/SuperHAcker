# 4.​ Create a simple client-server program using socket.

import socket

client_socket = socket.socket()

client_socket.connect(('127.0.0.1',2322))

print(client_socket.recv(1024).decode())

client_socket.close()