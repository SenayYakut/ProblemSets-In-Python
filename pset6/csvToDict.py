import csv
from sys import argv, exit

if len(argv) != 2:
    print("missing-commandline-argument")
    exit(1)
        
with open(argv[1])as csv_file:
    reader = csv.DictReader(csv_file)
    dict_list = []
    for row in reader:
        dict_list.append(row)
print(dict_list)
        