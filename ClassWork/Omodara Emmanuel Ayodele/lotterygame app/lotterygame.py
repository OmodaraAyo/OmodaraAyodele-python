#import randint from random to generate random numbers less than 1000 and greater than or equals 100(random = randint(100, 1000)
#prompt user to enter three digit number and store it in a variable 
#if user enters a number less than 100 or greater than 1000, break.
#else if user enters a number greater than, equals to 100 and less than 1000, check the number and compare the random number generated...
#if user Input matches random number generated in exact order (award: $10,00)
#else if user input matches all numbers in random number (award: $3000)
#else if none or one of user Input number matches a digit in random number generated (award: $0)


from random import randint

random = randint(100, 1000)
random_Digit1 = random // 100
random_Digit2 = (random // 10) % 10
random_Digit3 = random % 10
print(random)
user_Input = int (input('Enter three-digit number: '))

if user_Input < 100 or user_Input >= 1000:
		print('Three-digit number only.')

elif user_Input >= 100 and user_Input < 1000:  
	new_Number = user_Input
	
	new_Number1 = new_Number // 100
	new_Number2 = (new_Number // 10) % 10
	new_Number3 = new_Number % 10
	
	if user_Input == random:
		print (f'Congratulations!!! \naward: $10,000')

	elif (new_Number1 == random_Digit1 and new_Number2 == random_Digit3 and new_Number3 == random_Digit2):
			print (f'Congratulations!!! \naward: $3,000')
	
	elif (new_Number1 == random_Digit2 and new_Number2 == random_Digit1 and new_Number3 == random_Digit3):
			print (f'Congratulations!!! \naward: $3,000')
	
	elif (new_Number1 == random_Digit2 and new_Number2 == random_Digit3 and new_Number3 == random_Digit1):
			print (f'Congratulations!!! \naward: $3,000')
	
	elif (new_Number1 == random_Digit3 and new_Number2 == random_Digit1 and new_Number3 == random_Digit2):
			print (f'Congratulations!!! \naward: $3,000')
	
	elif (new_Number1 == random_Digit3 and new_Number2 == random_Digit2 and new_Number3 == random_Digit1):
			print (f'Congratulations!!! \naward: $3,000')
	
	else:
		print(f'Ticket lost... \naward: $0')

	



	