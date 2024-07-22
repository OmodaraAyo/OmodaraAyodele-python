def singletaxcalculator(taxableIncome):

	
		if taxableIncome <= 0:
			return 0
	
		elif taxableIncome > 0 and taxableIncome <= 8350:
			return taxableIncome * 10/100

		elif taxableIncome > 8350 && taxableIncome <= 33950:
			return taxableIncome * 15/100
		
		elif taxableIncome > 33950 && taxableIncome <= 82250:
			return taxableIncome * 25/100

		elif taxableIncome > 82250 && taxableIncome <= 171550:
			return taxableIncome * 28/100

		elif taxableIncome > 171550 && taxableIncome <= 372950:
			return taxableIncome * 33/100
	
		elif taxableIncome > 372950:
			return taxableIncome * 35/100

		else
			return 0


	