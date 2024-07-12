userInput = int (input ('Press -1 to exit or select a number to perform a transaction...  \n1. Deposit 	2. Withdraw	3. Balance: '))

totalBalance = 0
counter = 0

while userInput != -1 and userInput >= 1:
	
	if userInput == 1:
		deposit = float (input ("Deposit: $"))
		if deposit > 0:
			totalBalance += deposit
			counter += 1
			print ('Successful.')
		elif deposit <= 0:
			print ('Failed')

	if userInput == 2:
		Withdraw = float (input ("Withdraw: $"))
		if Withdraw < 1:
			print ('Invalid amount')

		elif  Withdraw > totalBalance:
			print ('Failed')

		elif totalBalance > 0 and totalBalance >  Withdraw:
			totalBalance = totalBalance - Withdraw
			print ('Successful!')
			print ('Please take your cash...')

	if userInput == 3: 
		if totalBalance < 0:
			print ('Insufficient balance')

		else:
			 print ('Balance: $',"%.2f" % totalBalance)

	if userInput != 1 or userInput != 2 or userInput != 3:
		print ('')

	userInput = int (input ('1. Deposit 	2. Withdraw	3. Balance: '))
		
		
if userInput == -1:
	print ('App closed')
		
		