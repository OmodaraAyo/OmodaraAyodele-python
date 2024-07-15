print ('Result > 40 = Pass, Below 40 = Failed. (1 = Pass, 2 = Failed)')
print ('Enter -1 to exit.\n')
userInput = int (input('Enter your grade: '))

passes = 0
failed = 0
while userInput != -1:

	if userInput == 1:
		passes += 1
	
	elif userInput == 2:
		failed += 1

	
	userInput = int (input('Enter your grade: '))

totalNumberOfStudent = passes + failed

if userInput == -1:
	print('\nTotal number of student:',totalNumberOfStudent)
	print(passes,'of the student passed.')
	print(failed,'of the student failed.')
	if passes > 8:
		print('Bonus to instructor')