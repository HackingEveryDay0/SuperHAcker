vowels = {'a':0, 'e': 1, 'i': 2, 'o':3, 'u':4}
password = "P@ssw0rd"
newPass = ""
for index, char in enumerate(password):

    if char.lower() in vowels:
        newPass += "*"
    else: 
        newPass += char
    
print("Result: ", newPass)
