from sys import argv
import csv

if not len(argv) == 3:
    print("Usage: python dna.py data.csv sequence.txt")

with open(argv[1], "r") as csvfile:
    reader = csv.reader(csvfile)
    row1 = next(reader)

comparison_list = []
sequence = open(argv[2])
sequence = sequence.read()
x = 0

for word in range(1, len(row1)):  # Iterating over each STR
    counter1 = 0
    counter2 = 0
    i = 0
    j = len(row1[word])
    k = len(row1[word])
    while not j == len(sequence):  # Checking for a match between row1[1] and sequence[i:j]
        if not sequence[i:j] == row1[word]:  # If no match, move on to next set of chars
            i += 1
            j += 1
        elif sequence [i:j] == row1[word]:  # If match, incremenet i & j by length of row1[1] to check next set of chars
            i += k
            j += k
            if sequence [i:j] == row1[word]:  # If another match, incrementing counter and move on to checking again
                counter2 += 1
            else:
                counter2 += 1  # If no more matches, add one for inital match skipped
                if counter2 > counter1:  # If not, check if most in a row and if so, update counter1
                    counter1 = counter2
                counter2 = 0
    comparison_list.append(counter1)


with open(argv[1], "r") as csvfile:
    database = csv.DictReader(csvfile)
    for key in database:
        x = 0
        for word in range (1, len(row1)):
            if int(key[row1[word]]) == comparison_list[x]:
                x += 1
                if x == len(comparison_list):
                    print(f"{key['name']}")
                    exit()
    else:
            print("No match")