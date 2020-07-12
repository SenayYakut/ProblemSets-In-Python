'''
Write a program in Python which will add natural numbers up to 
'''

# get the number from user
n = int(input("Enter n: "))

#initialize a sum and a counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1

print("The sum of the natural numbers ", sum)

