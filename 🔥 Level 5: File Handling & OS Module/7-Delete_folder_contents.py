# Make a Python script that deletes all files in a directory (be careful!).

import os 
folder_dir = "./TestDir"
files = os.listdir(folder_dir)
print(files)
for file in files:
    os.remove(os.path.join(folder_dir,file))

