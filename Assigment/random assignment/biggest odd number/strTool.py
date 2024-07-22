def biggest_odd(number):
	largest = 0
	for value in number:
		new_value = int(value)
		if new_value % 2 != 0:
			new_number = str(new_value)
			for the_numbers in new_number:
				that_number = int (the_numbers)
				if that_number > largest:
					largest = that_number
	return largest

	
	

	