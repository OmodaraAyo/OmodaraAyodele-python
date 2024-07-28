#prompt user to enter number of feet and store
#ONE FOOT = 0.305
#to convert to meters use formular (user Input * ONE FOOT)
#output result.

import metercalculator
user_input = int (input('Enter number of feet: '))
result = (metercalculator.convert_to_meter(user_input))
print(f'{result:.3f} meters')