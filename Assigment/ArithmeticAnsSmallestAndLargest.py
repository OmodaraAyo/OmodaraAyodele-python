number = int (input ("Enter a number: "))
number2 = int (input ("Enter a number: "))
number3 = int (input ("Enter a number: "))

sum = number + number2 + number3
print ('\nSum =', sum )
average = (number + number2 + number3) / 3
print ('Average =', average)
product = number * number2 * number3
print ('product =', product )

if number > number2 and number > number3:
	print ( number, 'is the largest' )

elif number2 > number and number2 > number3:
	print ( number2, 'is the largest' )

elif number3 > number2 and numbe3r > number2:
	print ( number3, 'is the largest' )
else:
	print ('All numbers are equal')


if number < number2 and number < number3:
	print ( number, 'is the Smallest' )

elif number2 < number and number2 < number3:
	print ( number2, 'is the Smallest' )

elif number3 < number2 and numbe3r < number2:
	print ( number3, 'is the Smallest' )
else:
	print ('All numbers are equal')

