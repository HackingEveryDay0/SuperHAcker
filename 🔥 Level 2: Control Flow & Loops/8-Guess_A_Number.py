# Create a basic number guessing game.

import random

print("Welcome to the guessing number game, I will choose a between 1-100 and you guess it")
correct_num = random.randrange(1,100)

print("I choosed a number, guess what I've choosed")
user_num = None

while user_num != correct_num:
    user_num = int(input("Enter a Number: "))
    if user_num == correct_num:
        print(f"Correct the number is {user_num}")
    elif user_num > correct_num:
        print("Hint: you number is higher than the correct num")
    else:
        print("Hint:  you number is smaller than the correct num")
    print("*"*30)
