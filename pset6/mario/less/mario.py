
#Write, in a file called mario.py in ~/pset6/mario/less/, a program that recreates the half-pyramid using hashes (#) for blocks, exactly as you did in Problem Set 1, except that your program this time should be written (a) in Python and (b) in CS50 IDE.
#To make things more interesting, first prompt the user with get_int for the half-pyramid’s height, a positive integer between 1 and 8, inclusive.

#If the user fails to provide a positive integer no greater than 8, you should re-prompt for the same again.
#Then, generate (with the help of print and one or more loops) the desired half-pyramid.
#Take care to align the bottom-left corner of your half-pyramid with the left-hand edge of your terminal window.


num = int(input("Enter a height from 1 to 8 for the half of pyramid: "))

for i in range(1,num+1):
    print("  "*(num-i) +"# "*i)
        