userInput = int (input ("Enter Grade Score: "))

if userInput >= 75  and userInput <= 100:
	print ('A')

elif userInput >= 65:
	print ('B')

elif userInput >= 50:
	print ('C')

elif userInput >= 40:
	print ('D')

elif userInput < 40 and userInput >= 0:
	print ('F')
	