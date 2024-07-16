from random import randint
print ('')
start = input ('Press Start to lunch game or Stop to end game: ')
while start not in ['Stop']:
	print('Guess my Number between 1 and 1000 with the fewest guesses')
print ('')

	game = int (input('guess the number: '))

	random_number = randint(1,1001)
	number = 0
	while game != random_number:
			number += 1
			if game > random_number:
				print('Too High')
				print('Try again...')
			
			elif random_number > game:
				print('Too Low')
				print('Try again...')
			
			game = int (input('guess the number: '))
			print('')
	if game == random_number:
		print('Congratulations!!! You guessed the number!')
		print(f'The number is {random_number}')
		print(f'Number of attempt is {number}')	
	
	start = input ('Press Start to play again or Stop to end game: ')

print ('App closed')