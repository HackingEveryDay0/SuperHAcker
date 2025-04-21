import socket

domain_name = str(input("Enter the domain name: "))

try: 
    ip = socket.gethostbyname(domain_name)
    print(f"Hostanme of {domain_name} is {ip}")
except:
    print("invalid domain name")

