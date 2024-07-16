passes = 0
failed = 0
for student in range(15):

	scores = int (input('Enter score: '))

	if scores > 45 and scores < 100:
		passes += 1

	elif scores < 45 and scores > 0:
		failed += 0

print(f'Number of student that passed: {passes}')
print(f'Number of student that failed: {failed}')