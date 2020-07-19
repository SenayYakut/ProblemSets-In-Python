import csv
from sys import argv, exit


if len(argv) != 3:
    print("missing command_line argument")
    exit(1)



# Opening the csv file and reading its content into the memory

with open(argv[1], "r") as csv_file:
    reader = csv.DictReader(csv_file)
    dict_list =[]
    for row in reader:
        dict_list.append(row)
# print(dict_list)

with open(argv[2], "r") as txt_file:
    s = txt_file.read()
    AGATC = s.count("AGATC")
    TTTTTTCT = s.count("TTTTTTCT")
    AATG = s.count("AATG")
    TCTAG = s.count("TCTAG")
    GATA = s.count("GATA")
    TATC = s.count("TATC")
    GAAA = s.count("GAA")
    TCTG = s.count("TCTG")
    dict_l = []
    dict_l.append(AGATC)
    dict_l.append(TTTTTTCT)
    dict_l.append(AATG)
    dict_l.append(TCTAG)
    dict_l.append(GATA)
    dict_l.append(TATC)
    dict_l.append(GAAA)
    dict_l.append(TCTG)
    print(dict_l)