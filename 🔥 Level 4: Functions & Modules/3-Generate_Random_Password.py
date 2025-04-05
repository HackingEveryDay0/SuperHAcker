# Write a function that generates a random password of 12 characters.
import random
import string 
result = ""
for i in range(1,13):
    result += random.choice(string.ascii_letters)

print("Generated 12 char random Password: ", result)
