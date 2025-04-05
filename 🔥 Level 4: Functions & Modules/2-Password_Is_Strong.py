# Create a function that checks if a password is strong (at least 8 characters, includes a number, and a special character).
import re

def isStrongPassword(password):
    if len(password) < 8:
        return False
    if not re.search(r'\d',password):
        return False
    if not re.search(r"[^\w]", password):
        return False
    
    return True

print("Check if your password is strong: ")

entered_password = str(input("Enter Password: "))

print("-"*10)

if isStrongPassword(entered_password):
    print("Your Password is Strong")
else:
    print("Your Password Isn't Strong")
