# Use the hashlib module to create an MD5 hash of a user-entered string.
import hashlib

print("Enter a text so I can Hash it for you :)")
print("-"*10)
entered_text = str(input(("Enter a text: ")))

h = hashlib.md5()
h.update(entered_text.encode())

print("-"*10)
print("Your text: ", entered_text)
print("MD5 Hashed Text: ", h.hexdigest())