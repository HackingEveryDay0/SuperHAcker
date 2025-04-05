# ​ Write a function that checks if an IP address is valid.
import re

print("THIS PROGRAM IS TO CHECK IF AN IP ADDRESS VALID OR NOT")
print("-"*10)

entered_ip = str(input("Enter an IP address: "))

# valid IP v4 [0-255].[0-255].[0-255].[0-255]
pattern_ipv4 = r"^(?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d)$"

if re.search(pattern_ipv4, entered_ip):
    print("Valid IP ")
else:
    print("Note a valid IP Address")

