'''
DNA Implement a program that identifies a person based on their DNA, per the below.

'''

import csv
from sys import argv, exit

# Calculate the max number of time sub string  consequtively repeated

def get_maximum_number_of_times_substring(s, sub):
    ans = [0] * len(s)
    for i in range(len(s) - len(sub), -1, -1):
        if s[i: i + len(sub)] == sub:
            if i + len(sub) > len(s) - 1:
                ans[i] = 1
            else:
                ans[i] = 1 + ans[i + len(sub)]
    return max(ans)


def print_match(reader, actual):
    for line in reader:
        person = line[0]
        values = [int(val) for val in line[1:]]
        if values == actual:
            print(person)
            return
    print("No match")         
        
# Opening the csv file(it is the second comand-line argument, index first) and reading it's content into memory

def main():
    
    # Verifying if the user provided correct number of command-line arguments
    if len(argv) != 3:
        print("missing command-line argument")
        exit(1)    
    with open(argv[1]) as csv_file:
        reader = csv.reader(csv_file)
        # for row in reader:
        #   print(row)
        all_sequences = next(reader)[1:]
        # Opening the txt file and reading its content into memory
        with open(argv[2]) as txt_file:
            s = txt_file.read()
            actual = [get_maximum_number_of_times_substring(s,seq) for seq in all_sequences]

        print_match(reader, actual)


if __name__ == "__main__":
    main()

