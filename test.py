from itertools import count


introString = input("Enter your intro: ")
characterCount = 0
wordCount = 1
for i in introString:
    characterCount = characterCount + 1
    if(i == " "):
        wordCount += 1

print("No. of words: ", wordCount)
print("No. of characters: ", characterCount)