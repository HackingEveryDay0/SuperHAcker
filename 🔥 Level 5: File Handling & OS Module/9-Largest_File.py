# 9.​ Find the largest file in a directory.

import os 


print("Enter folder path") 
path = os.path.abspath(input()) 

size = 0

max_size = 0

max_file ="" 

for folder, subfolders, files in os.walk(path): 
	
	for file in files: 
		size = os.stat(os.path.join( folder, file )).st_size 
		
		if size>max_size: 
			max_size = size 
			max_file = os.path.join( folder, file ) 

print("The largest file is: "+max_file) 
print('Size: '+str(max_size)+' bytes') 
