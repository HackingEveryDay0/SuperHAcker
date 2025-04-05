# Write a program that counts how many times each letter appears in a string.

entered_text = str(input("Enter a text: "))
letter_counter = {}
for letter in entered_text:

    if letter not in letter_counter:
        letter_counter[letter] = 1
    elif letter in letter_counter:
        letter_counter[letter] = int(letter_counter[letter]) + 1

print("*"*10)
print("OUTPUT: ")
print(letter_counter)   
