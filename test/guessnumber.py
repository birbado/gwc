#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: 

print(aRandomNumber)

guess = input("Guess a number between 1 and 20 (inclusive): ")
while (guess != aRandomNumber):
    guess = int(guess)
    if (guess < aRandomNumber):
        print ('higher!')
        guess = input('guess another number!')
    elif (guess > aRandomNumber):
        print ('lower!')
        guess = input('guess another number!')
    else:
        print ('thats correct!')
       