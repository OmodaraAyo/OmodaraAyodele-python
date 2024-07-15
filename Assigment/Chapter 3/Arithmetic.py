print('Enter three integers and get their sum, average, product, the smallest and largest number...')

sum = 0
average = 0
product = 1
smallest = 0
Largest = 0
for userInput in range(4):
	userInput = int (input('Enter a number: '))
	if userInput > Largest:
		Largest = userInput
	elif userInput <= smallest:
		smallest = userInput
	sum += userInput
	product = product * userInput
	average = sum / 4
		
print('\nSum =', sum)
print('Average =', average)
print('Product =', product)
print('The smallest number is',smallest)
print('The largest number is',Largest)


