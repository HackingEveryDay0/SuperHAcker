entered_text = input("Enter a text : ")

left, right = 0, len(entered_text) - 1

while left <= right:
    if entered_text[left] == entered_text[right]:
        left +=1
        right -= 1
    else:
        print("Not Palindrome")
        break
if left >= right:
    print("text is palindrome")