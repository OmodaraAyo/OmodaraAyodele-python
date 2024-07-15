print ('Enter five digit integers')
print('')

number = int (input('Enter number: '))

if number // 1000000 == 0 and number % 1 == 0:
		print("It's a palindrome")

else:
	print('It is not a palindrome')