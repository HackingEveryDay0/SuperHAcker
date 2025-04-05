# Write a function that finds the longest word in a list.

def Find_Longest_Word(words):
    maxWordIndex = 0
    for index, value in enumerate(words):
        if len(value) > len(words[maxWordIndex]):
            maxWordIndex = index
    return words[maxWordIndex]

words = ["SuperHacker", "HackTheWorld","FreePalastine","HackingEveryDay"]
print("List: ", words)

longestWord = Find_Longest_Word(words)
print("Longest Word: ", longestWord)
