def only_floats (a,b):
	
	counter = 0
	if (a is float(a)):
		counter +=1
	elif (b is float(b)):
		counter += 1
	else:
		counter = 0
	return counter
