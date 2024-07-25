def fahrenheit_calculator(Celsius):

	fahrenheit = (9 / 5) * Celsius + 32
	return fahrenheit

temperature = int (input('Enter Temperature: '))
if temperature >= 0 and temperature <= 100:
	print("Celsius", "\t", "fahrenheit")
	for number in range(0,101):
		result = fahrenheit_calculator(number)
		print (f'{number}\t\t {result:.1f}')
	
else:
	print("Invalid input")