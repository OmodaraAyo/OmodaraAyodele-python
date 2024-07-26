#prompt user to enter number of feet and store
#one foot = 0.305
#to convert to meters use formular (user Input * one foot)
#output result.


def convert_to_meter(feet):
	one_foot = 0.305
	return feet * one_foot

user_input = int (input('Enter number of feet: '))
result = convert_to_meter(user_input)
print(f'{result:.3f} meters')