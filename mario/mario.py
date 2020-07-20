from cs50 import get_int

size = get_int("Height:")

while not size in range(1, 9, 1):
    size = get_int("Height:")

i = 0
j = 1
k = size - 1

for x in range(size):
    for x in range(j, size):  # Printing spaces using for loop
        print(" ", end="")

    for x in range(k, size):  # Printing hashes using for loop
        print("#", end="")

    print("  ", end="")  # Printing two spaces to separate half-pyramids

    for x in range(k,size):  # Printing second set of hashes using for loops
        print("#", end ="")
    print("")  # Printing a line break
    i += 1  # Iterating the numbers in order to allow for printing correct number of # / spaces
    j += 1
    k -= 1