print ('Check the cost of your road tax')
print('')

open_app = input ("Type 'Start' to launch application or 'Stop' to close application: ")
while open_app.lower() != 'start' and open_app.lower() != 'stop':
		print ('Wrong input...')
		open_app = input ("Type 'Start' to launch application or 'Stop' to close application: ")

ROAD_TAX1 = 10 / 100
ROAD_TAX2 = 15 / 100
ROAD_TAX3 = 20 / 100
ROAD_TAX4 = 25 / 100


print('')
while open_app.lower() != 'stop':
	cost_Of_Car = int(input('Cost Of Vehicle: '))

	if cost_Of_Car == 0 and cost_Of_Car < 0:
		print('Invalid amount')

	elif cost_Of_Car <= 1000000 and cost_Of_Car > 0:
		road_tax = cost_Of_Car * ROAD_TAX1
		print(f'Road tax is #{road_tax}')

	elif cost_Of_Car > 1000000 and cost_Of_Car <= 3000000:
		road_tax = cost_Of_Car * ROAD_TAX2
		print(f'Road tax is #{road_tax}')

	elif cost_Of_Car > 3000000 and cost_Of_Car <= 5000000:
		road_tax = cost_Of_Car * ROAD_TAX3
		print(f'Road tax is #{road_tax}')

	elif cost_Of_Car > 5000000:
		road_tax = cost_Of_Car * ROAD_TAX4
		print(f'Road tax is #{road_tax}')
	
	open_app = input ("Type 'Start' to launch application again or 'Stop' to close application: ")
	print ('')
	while open_app.lower() != 'start' and open_app.lower() != 'stop':
		print ('Wrong input...')
		open_app = input ("Type 'Start' to launch application again or 'Stop' to close application: ")
		print('')

if open_app.lower() == 'stop':
	print ('Application closed')
		


	