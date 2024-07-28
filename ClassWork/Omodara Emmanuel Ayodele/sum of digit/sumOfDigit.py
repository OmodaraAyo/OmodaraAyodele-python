import get
user_input = int (input('Enter a number: '))
result = (get.sumOfDigitIn(user_input))
if result == 'error':
	print('Numbers between 0 and 1000 only.')
else:
	print(f'Sum of all digit = {result}')