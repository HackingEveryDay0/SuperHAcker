import socket

server_socket = socket.socket()

port = 2322

server_socket.bind(('',port))

server_socket.listen(5)
print("Socket Listening")

while True:
    client, ip = server_socket.accept()
    print("Connection from address: ", ip)

    client.send("Thank you for connecting :)".encode())

    client.close()

    break
server_socket.close()