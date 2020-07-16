import csv


name = input("Enter your name: ")
number = input("Enter your number: ")

with open("phonebook.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow((name, number))

