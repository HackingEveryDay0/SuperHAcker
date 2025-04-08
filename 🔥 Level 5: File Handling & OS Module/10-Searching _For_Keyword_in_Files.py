import os 

folder_path = str(input("Enter Folder path: "))
keyword = str(input("Enter Keyword to search: "))
isFound = False
files = os.listdir(folder_path)

for file in files:
    file = open(os.path.join(folder_path,file),'r')
    dict_words = {index:value for index,value in enumerate(file.read().split())}
    
    if keyword in dict_words.values():
        print(f"Keyword {keyword} found at ")
        print(f"File path: {folder_path}/{file.name}")
        isFound = True

if isFound == False:
    print(f"keyword {keyword} Not found in any files in the dir {folder_path}")
    