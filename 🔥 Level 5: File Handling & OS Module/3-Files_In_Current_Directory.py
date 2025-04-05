# Write a program that lists all files in the current directory.
import os

files = os.listdir(".")
print("\nFiles In Current Directory\n")

for file in files:
    print(file)