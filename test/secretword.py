import random

potential_words = ["example", "words", "someone", "can", "guess"]

word = random.choice(potential_words)

# Use to test your code:
print(word)

word = word.lower()

# Make it a list of letters for someone to guess
current_word = ["_", "_"] # TIP: the number of letters should match the word

# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ")
	if guess in word
		print ('theletter is in the word')

	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!

	print(current_word)

	else:
		fails = fails+1
		print("You have " + str(maxfails - fails) + " tries left!")