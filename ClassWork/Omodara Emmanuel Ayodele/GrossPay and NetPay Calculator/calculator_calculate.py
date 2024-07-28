def gross_pay(hours_Worked, hourly_pay_rate):
		return hours_Worked * hourly_pay_rate

def federal_withholding(hours_Worked, hourly_pay_rate):
		gross_pay = hours_Worked * hourly_pay_rate
		federalWithholding = gross_pay * 0.20
		return federalWithholding

def state_withholding(hours_Worked, hourly_pay_rate):
		gross_pay = hours_Worked * hourly_pay_rate
		stateWithholding = gross_pay * 0.09
		return stateWithholding


