def only_floats (a,b):
		counter = 2
		new_number = float(a)
		new_number2 = float(b)
		if new_number and new_number2 is type(float):
			counter += 1
		else:
			counter += 0
		return counter