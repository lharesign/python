from cs50 import get_float
import math

cash = get_float("Change owed: ")
while not cash >= 0:
    cash = get_float("Change owed: ")

dollars = math.trunc(cash)  # Calculating number of full dollars
remaining_cents = (round((cash - dollars) * 100))  # Calculating number of cents remaining once dollars removed
cash = (round(dollars * 100) + remaining_cents)  # Calculating cash in cents format
coins = 0  # Creating a counter to track how many coins used

while cash > 0:  # While cash is greater than zero, carry out following if statements
    if cash >= 25:
        cash -= 25
        coins += 1
    elif cash < 24 and cash >= 10:
        cash -= 10
        coins += 1
    elif cash < 10 and cash >= 5:
        cash -= 5
        coins += 1
    else:
        cash -= 1
        coins += 1

print(coins)  # Print out the numbers of coins it took to reach zero