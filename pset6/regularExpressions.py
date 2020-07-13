'''
Write a program in python which will ignore any unwanted chars and mistakes in user input
'''

import re

s = input("Do you agree?\n")

if re.search("^y(es)?", s, re.IGNORECASE):
    print("Agreed.") 
elif re.search("^n(o)?", s, re.IGNORECASE):
    print("Not Agreed.")
        