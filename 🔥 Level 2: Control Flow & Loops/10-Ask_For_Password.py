# Use a while loop to continuously ask for a password until the correct one is entered.
correct_password = "strongPass"
entered_password = None

while correct_password != entered_password:
    entered_password = str(input("Enter the password : "))

    if correct_password == entered_password:
        print("Correct Password")
        break


