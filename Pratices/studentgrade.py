passes = 0
failed = 0
number_of_student = 15
for student in range(1, 16):
	student_Grade = int (input('Enter score: '))
	if student_Grade >= 45 and student_Grade <= 100:
		passes += 1
	elif student_Grade < 45 and student_Grade > 0:
		failed += 1

print(f'Total number of student = {number_of_student}')
print (f'The number of student who passed = {passes}')
print(f'The number of student who failed = {failed}')