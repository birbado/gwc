#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: 

print(aRandomNumber)

guess = input("Guess a number between 1 and 20 (inclusive): ")
while (guess != aRandomNumber):
    guess = int(guess)
    if not guess.isnumeric():
	    print("That's not a positive whole number, try again!")
    elif (guess < aRandomNumber):
            print ('higher!')
    elif (guess > aRandomNumber):
            print ('lower!')
    else:
        print ('thats correct')
guess = input('guess another number!')