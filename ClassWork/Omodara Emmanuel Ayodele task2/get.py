def even_Or_Odd_Numbers(user_Input):
		if user_Input % 2 == 0:
			return 'It is an even number.'
		elif user_Input % 2 != 0:
			return 'It is an odd number.'
		else:
			return 0

def reverse_Number(user_Input):
	reverse = 0
	while user_Input > 0:
		reverse = (reverse * 10) + (user_Input % 10)
		user_Input = user_Input / 10
	return reverse

def sum_Of_strings(user_Input1, user_Input2):
		user_Input1 = str.toInteger(user_Input1)
		user_Input2 = str.toInteger(user_Input2)
		sum = first_length + second_length
		return sum

