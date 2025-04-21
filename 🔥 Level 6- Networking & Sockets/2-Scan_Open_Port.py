# 2.​ Use socket to scan open ports on scanme.nmap.org for ports 20-100.

import socket
target_ip = socket.gethostbyname("scanme.nmap.org")
#                                ipv4           TCP
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for port in range(20,101):
    try:
        my_socket.connect((target_ip,port))
        print(f"IP: {target_ip}, Port {port} open")
    except:
        print(f"IP: {target_ip}, Port {port} closed")


