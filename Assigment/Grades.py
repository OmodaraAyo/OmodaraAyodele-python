grade = int (input ('Enter your grade score: ') )

if grade >= 85 and grade <= 99:

	print ( 'Congratulations! Your grade of', grade, 'earns you an A in this course' )

elif grade >= 70:

	print ( 'Congratulations! Your grade of', grade, 'earns you an B in this course' )

elif grade >= 60:
	print ( 'Congratulations! Your grade of', grade, 'earns you an C in this course' )

elif grade >= 50:
	print ( 'Congratulations! Your grade of', grade, 'earns you an D in this course' )

elif grade <= 40 and grade >= 0:
	print ( 'oops! Take the course again' )
else:
	print ('Enter a valid score')