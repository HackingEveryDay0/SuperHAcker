# Write a function that takes a hostname and resolves it to an IP address.
import socket
def write_hostname():
    hostname = str(input("Enter a hostname: "))

    result = socket.gethostbyname(hostname)

    print("Result IP Address: ", result)

write_hostname()
