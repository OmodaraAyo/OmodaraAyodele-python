userInput = int (input ('Enter a number:'))
print('')

for counter in range(1, 11):
	result = userInput * counter
	print(f'{userInput} X {counter} = {result}')