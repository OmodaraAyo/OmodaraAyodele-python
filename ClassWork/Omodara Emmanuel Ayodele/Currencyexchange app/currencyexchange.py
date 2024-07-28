#prompt user to enter 0 to convert usd to naira or 1 to convert naira to usd and store user input
#declare a sentinel loop that checks if user input is 0 or 1 to convert from usd to naira or vise versa but if user input does not equal 0 or 1 continue to prompt user to enter either 0 or 1.
#if user input = 0, prompt the user again for 'amount' they would like to convert from usd to naira and store result.
#but if user input = 1, prompt the user again for 'amount' they would like to convert from naira to usd and store result.
#output result of either user input = 1 or result of user input = 1


import currencyexchangecalculator

user_input = int (input('Enter 0 to convert U.S dollars to Naira || Enter 1 to convert Naira to U.S dollars: '))
print()

while user_input != 0 and user_input != 1:
		print('Wrong input! Try again...')
		user_input = int (input('Enter 0 to convert U.S dollars to Naira || Enter 1 to convert Naira to U.S dollars: '))
		print('')

if user_input == 0:
	currency = float (input('Enter amount: $'))
	amount_to_naira = (currencyexchangecalculator.usd_to_naira(currency))
	print(f'#{amount_to_naira:.2f}')

if user_input == 1:
	currency = float (input('Enter amount: #'))
	amount_to_usd = (currencyexchangecalculator.naira_to_usd(currency))
	print(f'${amount_to_usd}')