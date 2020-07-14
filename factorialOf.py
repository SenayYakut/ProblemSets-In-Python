'''
Write a program which will print factorial of given number
'''
num = int(input("Enter a number: "))
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))

       
print("The factorial of", num, "is", factorial(num))
