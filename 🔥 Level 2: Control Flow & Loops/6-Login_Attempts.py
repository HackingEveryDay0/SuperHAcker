correct_username = "user"
correct_password = "password"

max_attempts = 3
attempts_left = max_attempts

while attempts_left > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == correct_username and password == correct_password:
        print("Login successful! Welcome,", username)
        break 
    else:
        attempts_left -= 1 
        if attempts_left > 0:
            print(f"Login failed. {attempts_left} attempts remaining.")
        else:
            print("Login failed. You have been locked out after 3 incorrect attempts.")

if attempts_left == 0:
    print("Please contact support to unlock your account.")