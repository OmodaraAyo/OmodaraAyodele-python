import calculator
			
user_Input = int (input('Enter subTotal: '))
user_Input2= int (input('Enter gratuity rate: '))
gratuity =  (calculator.calculate_gratuity_valueOf(user_Input2))
sub_Total = (calculator.calculate_total_valueOf(user_Input, gratuity))
print(f'Gratuity = {gratuity} \nTotal = {sub_Total}')
