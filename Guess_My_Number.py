# Program Name:
# Author:
# Date:

# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random  

#Opening Remarks
print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = input("Guess: ")# Create the priming read here
tries = 1

# guessing loop
while guess != the_number:
    #put the guessing game logic here
    if guess > the_number:
        print("Too high")
    elif guess < the_number:
        print("Too low")
    tries += 1
    guess = input("Guess: ") #Create the following read here


print("You guessed it!  The number was", the_number)
print("And it only took you", tries, "tries!\n")

#Program Closing  
input("\n\nPress the enter key to exit.")
