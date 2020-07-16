
# Write a program in Python using Regular Expressions which will print the count of all alphabetic characters in a given text 

import re

text = input("Enter the text: ")
    

def letterCount(text):
    pattern = "\w"
    countOfLetter = re.findall(pattern, text)
    return len(countOfLetter)

print(letterCount(text))