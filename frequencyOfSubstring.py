'''
Write a program in Python which  prints a substring in a string how many times occurs
'''

def main(string, sub_str):
    res =string.count(sub_str)
    return res
print(main("Geeksforgeeks is for geeks".lower(), "Geeks".lower()))
    
    