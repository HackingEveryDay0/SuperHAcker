# 5.​ Write a program that resolves a domain name to an IP address.

import socket

domain_name = str(input("Enter the domain name: "))

try: 
    ip = socket.gethostbyname(domain_name)
    print(f"Hostanme of {domain_name} is {ip}")
except:
    print("invalid domain name")

