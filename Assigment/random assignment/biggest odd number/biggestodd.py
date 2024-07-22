import strTool

number = input('Enter number: ')
largest = (strTool.biggest_odd(number))
if largest == 0:
	print('There is no odd number.')
else:
	print ("Largest odd number is",largest)