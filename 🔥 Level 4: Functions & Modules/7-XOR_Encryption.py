# # 7.​ Build a function that performs a simple XOR encryption on text.

# """
# Here is how I'm planing of solving this:
#     1- let the user input a text for encryption or decryption (both their operations are the same :) 
#     2- Take every character of the text and converted into binary using bin()
#     3- make an ORX operation using key = 00000010
#     4- convert the encrytped char into asci letter again

#     Do the above for each char
# """


def encrypt_or_decrypt(text):
    modified_text = []

    for char in entered_text:

        asci_letter = ord(char)
        oxr_result_decimal = asci_letter ^ int(key,2)
        char_result = chr(int(oxr_result_decimal))
        modified_text.append(char_result)

    return "".join(modified_text)


key = "00000010"
option_num = None


while option_num != 0:
    print("Options")
    print("-"*10)
    print("1- Encrypt a Message\n2- Decrypt a Message\n0- Exist")

    option_num = int(input("Enter Option Number: "))

    if option_num == 1:
        entered_text = str(input("Enter text to encrypt: "))
        encrypted_text = encrypt_or_decrypt(entered_text)

        print("-"*10)
        print("\n\nEncrypted Text\n\n")
        print("-"*10)
        print("\n")
        print("".join(encrypted_text))
        print("\n")
        print("-"*10)
    elif option_num == 2:
        entered_text = str(input("Enter text to Decrypt: "))
        decrypted_text = encrypt_or_decrypt(entered_text)

        print("-"*10)
        print("\nDecrypted Text\n\n")
        print("-"*10)
        print("\n")
        print("".join(decrypted_text))
        print("\n")
        print("-"*10)

    elif option_num == 0:
        print("GoodBye :) ")

    else:
        print("**INVALID OPTION, MAKE SURE YOU ENTER A NUMBER**")
