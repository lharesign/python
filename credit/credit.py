from cs50 import get_int
import math

card = get_int("Number: ")
card_length = int(math.log10(card)) + 1

card_number = str(card)  # Converting card number to string to access digits
checksum = 0  # Calculating checksum value
ends_zero = False

  # Calculating below whether sum of digits as per Luhn's algorithm ends with 0.

i = len(card_number) - 2  # Equating i to the penultimate digit and then iterating backwards to multiply value by 2 and add, skipping every other digit
while i >= 0:
    to_add = int(card_number[i]) * 2
    if to_add > 9:
        to_add = (to_add % 10) + ((to_add - (to_add % 10)) / 10)
    checksum += to_add
    i -= 2

k = len(card_number) - 1 # Equating i to the final digit and then iterating backwards to add value, skipping every other digit
while k >= 0:
    to_add = int(card_number[k])
    checksum += to_add
    k -= 2

if (checksum % 10 == 0):
    ends_zero = True

  # Calculating if valid cards

amex = math.trunc(card / 10000000000000)
mastercard = math.trunc(card / 100000000000000)
visa_thirteen = math.trunc(card / 1000000000000)
visa_sixteen = math.trunc(card / 1000000000000000)

if (card_length == 15 and amex == 37 and ends_zero == True) or (card_length == 15 and amex == 34 and ends_zero == True):
    print("AMEX")
elif card_length == 16 and mastercard >= 51 and mastercard <= 55 and ends_zero == True:
    print("MASTERCARD")
elif (card_length == 13 and visa_thirteen == 4 and ends_zero == True) or (card_length == 16 and visa_sixteen == 4 and ends_zero == True):
    print("VISA")
else:
    print("INVALID")
