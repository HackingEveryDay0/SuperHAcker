# ​ Write a script that creates a new text file, writes a message to it, and then reads it.
file_name = str(input("Enter File Name (e.g exampleFile)  "))
file_content = str(input("Enter File Content: "))

with open(f"{file_name}.txt", "w") as f:
    f.write(file_content)

file = open(f"{file_name}.txt")
content = file.read()
print("File Content")
print(f"{content}")