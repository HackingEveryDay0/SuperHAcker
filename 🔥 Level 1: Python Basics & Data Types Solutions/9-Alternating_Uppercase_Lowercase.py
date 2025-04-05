s = "H4ck3r"

resultList = []

for index, letter in enumerate(s):
    if index % 2 == 0:
        resultList.append(letter.lower())
    else: 
        resultList.append(letter.upper())
    
resultStr = "".join(resultList)
print("Result: ", resultStr)
