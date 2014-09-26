# Craps Roller
# Demonstrates random number generation
# Original Author: Michael Dawson
# Last Edited: Thorin Schmidt
# Date Edited: 9/26/2014

import random

# generate random numbers 1 - 6
die1 = random.randint(1, 6) 
die2 = random.randint(1, 6)

total = die1 + die2

string = "You rolled a " + str(die1) + " and a " +  str(die2) + " for a total of " + str(total)
print(string)

input("\nPress the enter key to exit.")
