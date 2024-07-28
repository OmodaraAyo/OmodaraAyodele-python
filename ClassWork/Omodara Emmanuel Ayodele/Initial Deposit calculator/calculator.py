def initial_deposit_calculator(final_account_value, monthly_interest_rate, number_of_month):

	initial_deposit_amount = final_account_value / (1 + monthly_interest_rate)** number_of_month
	return initial_deposit_amount
