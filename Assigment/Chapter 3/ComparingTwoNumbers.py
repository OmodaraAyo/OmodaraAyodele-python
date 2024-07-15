print ('Comparing two numbers...\n')

firstNumber = int (input('Enter a number: '))
secondNumber = int (input ('Enter a number:'))

if firstNumber != secondNumber and firstNumber > secondNumber:
			print(firstNumber, 'is not equal to', secondNumber, 'and it is greater than', secondNumber)
elif secondNumber != firstNumber and secondNumber > firstNumber:
	print(secondNumber, 'is not equal to', firstNumber, 'and it is greater than', firstNumber)

if firstNumber == secondNumber or secondNumber == firstNumber:
		print('Both number are equal.')