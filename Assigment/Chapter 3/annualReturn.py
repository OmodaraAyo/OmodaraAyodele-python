amount_invested = int (input('How much would you like to invest: '))
print ('\n')

investment_return = 0.70 

for years in range(1,31):
	annual_rate = (1 + investment_Return)**years
	amountDepositAtTheOfEachYear = (amount_Invested) * (annual_rate)

	print (f'Profit earned after {years} year -> {amountDepositAtTheOfEachYear:.2f}')