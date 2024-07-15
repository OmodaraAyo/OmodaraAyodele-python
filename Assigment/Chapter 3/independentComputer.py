medicalDiagnosis = input ('What is your problem: ')

userInput = input ('Have you had this problem before (Yes or No)? ')

while userInput not in ['Yes','No']:

		userInput = input ('Have you had this problem before (Yes or No)? ')

if (userInput == 'Yes'):
	print('Well, you have it again.')

if (userInput == 'No'):
	print('Well, you have it now.')	