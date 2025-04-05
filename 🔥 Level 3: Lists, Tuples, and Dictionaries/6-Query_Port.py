ports_services ={
7: "Echo service",
    20: "File Transfer Protocol data transfer",
    21: "File Transfer Protocol (FTP) control connection",
    22: "Secure Shell, secure logins, file transfers (scp, sftp), and port forwarding",
    23: "Telnet protocol—unencrypted text communications",
    25: "Simple Mail Transfer Protocol, used for email routing between mail servers",
    53: "Domain Name System name resolver",
    69: "Trivial File Transfer Protocol",
    80: "Hypertext Transfer Protocol (HTTP) uses TCP in versions 1.x and 2. HTTP/3 uses QUIC, a transport protocol on top of UDP",
    88: "Network authentication system",
    102: "ISO Transport Service Access Point (TSAP) Class 0 protocol",
    110: "Post Office Protocol, version 3 (POP3)",
    135: "Microsoft EPMAP (End Point Mapper), also known as DCE/RPC Locator service, used to remotely manage services including DHCP server, DNS server, and WINS. Also used by DCOM",
    137: "NetBIOS Name Service, used for name registration and resolution",
    139: "NetBIOS Session Service",
    143: "Internet Message Access Protocol (IMAP), management of electronic mail messages on a server",
    381: "HP data alarm manager",
    383: "HP performance data collector",
    443: "Hypertext Transfer Protocol Secure (HTTPS) uses TCP in versions 1.x and 2. HTTP/3 uses QUIC, a transport protocol on top of UDP",
    464: "Kerberos Change/Set password"
}

query_port = int(input("Query by Port Number: "))
print("*"*10)
if query_port in ports_services:
    print("Port: ", query_port)
    print("Description: ", ports_services[query_port])
else:
    print("Description for this port isn't defined in the database")