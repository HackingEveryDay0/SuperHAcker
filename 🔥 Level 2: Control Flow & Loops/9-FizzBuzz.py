# Print numbers 1-100, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and both with "FizzBuzz".

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} : FizzBuzz")
    elif i % 3 == 0:
        print(f"{i} : Fizz")
    elif i % 5 == 0:
        print(f"{i} : Buzz")


