print('Multiplication of factorial of an integer...')
print('')
userInput = int (input('Enter an integer: '))

factorial = 1
if userInput < 0:
	print(f'Invalid input')

elif userInput == 0:
	print(f'The multiplication of factorial of {userInput} is {factorial}')

elif userInput >= 1:
	for counter in range(userInput, 0, -1):
		factorial = factorial * counter
	print(f'The multiplication of factorials of {userInput} is {factorial}')