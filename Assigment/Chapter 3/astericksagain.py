for row in range(11):
	for column in range(row):
		print('*', end='' )
		
	print('')

print ('')	
for newrow1 in range(10, 0, -1):
	for newcolumn1 in range(newrow1):
		print('*', end='' )
		
	print('')

print ('')
N = 10
for newrow in range(10, 0, -1):
	for space in range (0, (N - newrow)):
		print (' ', end='')
	for newcolumn in range(newrow):
		print(f"{'*':}", end= '')
	
	print('')
