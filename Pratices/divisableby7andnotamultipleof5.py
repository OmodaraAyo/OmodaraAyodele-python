number = 771
number2 = 4201

for result in range(number, number2):
		if result % 7 == 0 and result % 5 != 0:
			print (f'{result},', end=' ')