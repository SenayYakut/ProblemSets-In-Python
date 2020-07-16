'''
Write a program in Python which will eliminate all of the white spaces from a given string
 '''
 
import re

string = """senay yakut, 415 -- ----,
  San Francisco, CA"""
  
pattern = "\s"
replace = ""

result = re.sub(pattern, replace, string)
print(result)