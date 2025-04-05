# Create a script that renames all .txt files in a folder to .bak.
import os
all_files = os.listdir(".")
for file in all_files:
    if file[-3:] == "txt":
         os.rename(file, file[:-3] + "bak")

# print(all_files)