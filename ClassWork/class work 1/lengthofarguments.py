def lengths_of_numbers(number):
		counter = 0
		for numbers in (number):
			counter += 1
		return counter

userInput = input('Enter a word: ')
result = lengths_of_numbers(userInput)
print(result)