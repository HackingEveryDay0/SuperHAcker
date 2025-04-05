dummy_users = {
    "user1": "password123",
    "john_doe": "qwerty2024",
    "alice99": "securePass!",
    "test_user": "letmein",
    "developer": "codeMaster42"
}
print("This program gets you the password of a user if it's exists")
print("-"*10)
query_user = str(input("Enter Username: "))

if query_user in dummy_users:
    print("-"*10)
    print("Username: ", query_user)
    print("Password: ", dummy_users[query_user])
    print("-"*10)

else:
    print("-"*10)
    print("USER NOT FOUND")
    print("-"*10)

