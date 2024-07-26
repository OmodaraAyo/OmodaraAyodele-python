for number in range (1, 21):
	print ('\t')
	for counter in range(1, 11):
		result = number * counter
		print(f'{number:>2} X {counter:>2} = {result:>4}')
		