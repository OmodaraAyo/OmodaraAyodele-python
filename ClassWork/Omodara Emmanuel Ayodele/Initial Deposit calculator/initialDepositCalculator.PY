import calculator

user_input = float (input('Enter final account value: $'))
ANNUAL_INTEREST_RATE = 56.04
MONTHLY_INTEREST_RATE = 4.67
user_input2 = int (input('Enter number of month: '))
initial_deposit_amount =(calculator.initial_deposit_calculator(user_input, MONTHLY_INTEREST_RATE, user_input2))
print(f'Initial deposit amount is ${initial_deposit_amount:.2f}')
