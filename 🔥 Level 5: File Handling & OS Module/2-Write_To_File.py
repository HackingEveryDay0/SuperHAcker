
# Create a script that logs user input to a file (keystroke.log).
content = str(input("Enter text to save it to file: "))

with open("keystroke.log", "w") as f:
    f.write(content)

print("Contents saved to file keystroke.log check it out :)")
