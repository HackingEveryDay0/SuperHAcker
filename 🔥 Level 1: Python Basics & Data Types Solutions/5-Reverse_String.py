s = "rekcah_repus"

rightPointer = len(s) - 1

reverseList = []

while rightPointer >= 0:
    reverseList.append(s[rightPointer])
    rightPointer -= 1

reverseStr = "".join(reverseList)
print(reverseStr)