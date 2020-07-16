import csv
from cs50 import get_string

name = get_string("Enter your name: ")
number = get_string("Enter your number: ")

with open("phonebook.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow((name, number))

#  Second way

import csv
from cs50 import get_string

name = get_string("Enter your name: ")
number = get_string("Enter your number: ")

file = open("phonebook.csv", "a")
writer = csv.writer(file)
writer.writerow((name, number))

file.close()

