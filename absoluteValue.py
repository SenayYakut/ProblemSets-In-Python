'''
Write a program which will print absolute value of the given number by user
'''

def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num
        
print(absolute_value(2))
print(absolute_value(-4))
