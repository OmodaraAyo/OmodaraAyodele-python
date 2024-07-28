def sumOfDigitIn(user_input): 
	
	if user_input >= 0 and user_input < 10:
		return user_input
		
	elif user_input >= 10 and user_input < 100:
		digit_One = user_input // 10
		digit_Two = user_input % 10
		sum = digit_One + digit_Two
		return sum

	elif user_input >= 100 and user_input <= 1000:
		digit_One = user_input // 100
		digit_Two = (user_input // 10) % 10
		digit_Three = (user_input // 1) % 10
		sum_Of_Digit = digit_One + digit_Two + digit_Three
		return sum_Of_Digit		

	else:
		return "error"
