from random import randint

start_game = input("Enter 'Start' to launch game or 'Stop' to end game: ")
random = randint(1, 1000)
print(random)
while start_game.lower() != Stop':
	print('Wrong input. Try again...')
	start_game = input("Enter 'Start' to launch game or 'Stop' to end game: ")
	if start_game.lower() == 'Start':
		userInput = int (input('Guess my number between 1 and 1000 with the fewest guesses: '))
	
		while userInput != random:	
			if userInput < random:
				print('Too low.')

			if userInput > random:
				print('Too high.')
	
			userInput = int (input('Try again: '))
		if userInput == random:
			print('Congratulations. You guessed the number!')

	start_game = input("Enter 'Start' to play again or 'Stop' to end game: ")

if start_game.lower() == 'Stop':
	print('App closed')
