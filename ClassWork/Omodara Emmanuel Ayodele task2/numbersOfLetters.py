user_Input = input('Write a sentence: ') 
number_Of_Alphabets = 0
number_Of_Digits = 0

for characters in user_Input:
	if characters == " " :
		number_Of_Alphabets += 1
	elif characters.lower() >= 'a' and characters.lower() <= 'z':
		number_Of_Alphabets += 1
	elif characters.lower() >= '0' and characters.lower() <= '9':
		number_Of_Digits += 1

print(f'{number_Of_Alphabets} Letters and {number_Of_Digits} Digits')
