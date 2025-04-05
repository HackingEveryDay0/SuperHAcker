# Write a function that reverses a string.

def Reverse_String(text):
    left , right= 0, len(text) -1

    textList = [letter for letter in text]

    while left < right:

        textList[left], textList[right] = textList[right], textList[left]

        left += 1
        right -= 1
    return "".join(textList)

entered_text = str(input("Enter a text that you want to reverse it: "))
print("-"*10)
print("Reversed text: ",Reverse_String(entered_text))
