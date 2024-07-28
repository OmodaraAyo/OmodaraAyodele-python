def years_In(user_Input):
	MINUTES_IN_A_YEAR = 525_600
	return user_Input // MINUTES_IN_A_YEAR
def days_In(user_Input):
	MINUTES_IN_A_YEAR = 525_600
	years = user_Input // MINUTES_IN_A_YEAR
	NUMBER_OF_MINUTES_IN_A_DAY = 1440 
	days = user_Input - (years * MINUTES_IN_A_YEAR)
	return days / NUMBER_OF_MINUTES_IN_A_DAY