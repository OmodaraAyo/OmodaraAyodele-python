print('-> 4.2% interest rate per month, 50% interest rate per annum...')
print('-> (@:line2) Press 1. For monthly Interest Rate 2. For annual Interest Rate.')
print ('-> Enter -1 to go back or close app')
print('')
annualInterestRate = 0.50
monthlyInterestRate = 0.042

principal = float (input ('How much would you like borrow: #'))
while principal != -1:
	interestRate = int (input('Monthly Interest Rate or Annual Interest Rate: '))
	while interestRate != -1:

		if interestRate == 1:
			duration = int (input ('How long until you pay back: '))
			if duration <= 0:
				print ('Invalid date')
				print('')
			else:
				numerator = monthlyInterestRate * (1 + monthlyInterestRate)**duration
				denominator = (1 + monthlyInterestRate)**duration 
				denominator2 = denominator - 1
				denominator3 = numerator / denominator2
				InterestRatePerMonth = principal * denominator3
				print ('')
				print (f'-> Your monthly payment is #{InterestRatePerMonth:.2f}')
				print ('')
	
		if interestRate == 2:
			duration = int (input ('How long until you pay back: '))
			if duration <= 0:
				print ('Invalid date')
				print('')
			else:
				numerator = annualInterestRate * (1 + annualInterestRate)**duration
				denominator = (1 + annualInterestRate)**duration 
				denominator2 = denominator - 1
				denominator3 = numerator / denominator2
				InterestRatePerMonth = principal * denominator3
				print ('')
				print (f'-> Your monthly payment is #{InterestRatePerMonth:.2f}')
				print('')

		print ("Enter '-1' to go back OR Select a number again...")
		print('')
		interestRate = int (input('Monthly Interest Rate or Annual Interest Rate: '))
	print('')
	print ("Enter '-1' to close app OR Borrow again")
	principal = float (input ('How much would you like borrow: #'))


if principal == -1 or interestRate == -1:
		print ('App closed')