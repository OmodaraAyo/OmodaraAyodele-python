def only_floats (a,b):
	
	counter = 0

	if (a is float(a)):
		counter +=1

	if (b is float(b)):
		counter += 1

	return counter

only_floats (66.5, 2)
only_floats (2, 1)
only_floats (66.5, 2.21)
only_floats (2, 66.34)