# Read a file and count how many times a given word appears.
import re
pattern = r"\w"

search_word = str(input("Enter word to see how much it appears in the test.txt file: "))
counter = 0
with open("test.txt", "r") as f:
    content = f.read()
    content_words = content.split()

    for word in content_words:
        if word.lower() == search_word.lower():
            counter += 1

    print("Number Of Appearance: ", counter)