print ('Separating the digit in an integer')
print ('Enter five digit integer\n')
userInput = int (input ('Enter number: '))

while userInput != -1:

	userInput1 = userInput // 10000
	userInput2 = (userInput // 1000) % 10
	userInput3 = (userInput // 100) % 10
	userInput4 = (userInput // 10) % 10
	userInput5 = userInput % 10
	print (userInput1, userInput2, userInput3, userInput4, userInput5)
	userInput = int (input ('Enter number: '))

if userInput == -1:
	print('App closed')