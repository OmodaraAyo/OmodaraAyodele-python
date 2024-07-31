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
		user_Input = user_Input // 10
	return reverse

def palindrome(user_Input):
	reverse = 0
	new_User_Input = user_Input
	while user_Input > 0:
		reverse = (reverse * 10) + (user_Input % 10)
		user_Input = user_Input // 10
	if new_User_Input == reverse:
		return "It is palindrome"
	else:
		return "It is not a palindrome"


def sum_Of_strings(user_Input1, user_Input2):
		user_Input1 = str.toInteger(user_Input1)
		user_Input2 = str.toInteger(user_Input2)
		sum = first_length + second_length
		return sum

def sorting_Numbers(user_Input, user_Input2, user_Input3):

			lowest_Number = 0
			middle_Number = 0
			largest_Number = 0
			if user_Input < user_Input2 and user_Input < user_Input3:
					lowest_Number = user_Input
			elif user_Input > user_Input2 and user_Input > user_Input3:
					largest_Number = user_Input
			else:
				middle_Number = user_Input

			if user_Input2 < user_Input and user_Input2 < user_Input3:
					lowest_Number = user_Input2
			elif user_Input2 > user_Input and user_Input2 > user_Input3:
					largest_Number = user_Input2
			else:
				middle_Number = user_Input2
			
			if user_Input3 < user_Input and user_Input3 < user_Input2:
					lowest_Number = user_Input3
			elif user_Input3 > user_Input and user_Input3 > user_Input2:
					largest_Number = user_Input3
			else:
				middle_Number = user_Input3
		
			return lowest_Number, middle_Number,largest_Number



