'''
 Write a program in Python which will return the odd numbers until any given range with dictionary comprehension
 '''
 
odds = {}
 
for x in range(11):
     if x % 2 != 0:
        odds[x] = x
print(odds)         