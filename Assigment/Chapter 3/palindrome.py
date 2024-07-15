print ('Enter five digit integers')
print('')

number = int (input('Enter number: '))

number1 = number // 10000
number2 = (number // 1000) % 10
number3 = (number // 100) % 10
number4 = (number // 10) % 10
number5 = number % 10

if number1 == number5 and number2 == number4:
		print ("It's a palindrome")
else:
	print ("It's not a palindrome")