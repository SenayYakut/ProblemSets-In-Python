import csv
from sys import argv, exit

if len(argv) != 2:
    print("missing command_line argument")
    exit(1)
else:
    exit(0)

names = []

with open('argv[0]','r') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    for row in csvReader:
        name = row[0]
        names.append(name)

with open('argv[1]','r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    for row in readCSV:
        for i in range(len(row)):
            row[]
        AGATC,TTTTTTCT,AATG,TCTAG,GATA,TATC,GAAA,TCTG