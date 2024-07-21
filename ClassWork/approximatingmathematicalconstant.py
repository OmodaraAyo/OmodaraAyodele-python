pi = 22 / 7
constant = 4
constanttwo = 3 
constantthree = constant / constanttwo

def infinite():
	number = 1
	while True:
		number = (number * constant) - constantthree
	constant2 += 2 
for number in infinite():
	print(f'{number}')
