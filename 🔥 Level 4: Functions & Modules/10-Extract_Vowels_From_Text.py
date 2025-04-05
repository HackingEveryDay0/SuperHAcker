# ​ Write a function that extracts all vowels “aeiouAEIOU” from a string.

def Extract_Voewels(text):
    vowels = {'a':0,'e':1,'u':2,'o':3,'i':4}
    text_list = [letter for letter in text]
    for index, letter in enumerate(text_list):
        if letter.lower() in vowels:
            del text_list[index]
        
    return "".join(text_list)

entered_text = str(input("Enter a text: "))
print("Text Without Vowels: ", Extract_Voewels(entered_text))


