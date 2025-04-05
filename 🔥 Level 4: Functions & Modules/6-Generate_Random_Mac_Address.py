
import re
import string
import random
# A MAC address consists of 48 bits, usually represented as a string of 12 hexadecimal digits (0 to 9, a to f, or A to F); these are often grouped into pairs separated by colons or dashes
# 00:1b:63:84:45:e6 or as 00-1B-63-84-45-E6.

# logic : It has 6 portion each portion represents 1 byte (8 bits) so from 0-255 value then convert that value into hexadecimal

def Generate_Random_MacAddress():
    mac_address = [random.randint(0,255) for _ in range(6)]

    for index, portion in enumerate(mac_address):
        mac_address[index] = str(f"{portion:02x}")
    print("Random Mac Address: ",":".join(mac_address))


Generate_Random_MacAddress()
