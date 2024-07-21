def root_and_remainder(a):
	
	if a % 5 == 0:
		return a**0.5
	
	elif a % 5 != 0:
		remainder = a % 5
		return remainder