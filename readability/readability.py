from cs50 import get_string
import math

input = get_string("Text: ")  # Receiving input from user
word_count = 0
char_count = 0
sentence_count = 0
nums = [ord(c) for c in input]  # Converting input to ASCII values

if nums[0] > 0:  # If first item in nums is more than zero, we have at least one word
    word_count = 1

for c in nums:  # Calculating character, word and sentence counts using ASCII values
    if (c >= 65 and c <= 90) or (c >= 97 and c <= 122):
        char_count += 1
    elif c == 32:
        word_count += 1
    elif c == 33 or c == 46 or c == 63:
        sentence_count += 1

average_letters = (char_count / word_count) * 100  # Calculating the CL Index
average_words = (sentence_count / word_count) * 100
cl_index = round((0.0588 * average_letters) - (0.296 * average_words) - 15.8)

if cl_index >= 16:  # Printing the respective grade
    print("Grade 16+")
elif cl_index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {math.trunc(cl_index)}")
