print ('Enter -1 to end...')
print('')
milesDriven = float (input('miles driven: '))
milesPerGallon = float (input('gallon used: '))

milesDrivenTotal = 0
gallonUsedTotal = 0

while milesDriven != -1 and milesPerGallon != -1:

	gallonUsedForEachMileDriven = milesDriven / milesPerGallon
	print(f'Mileage = {gallonUsedForEachMileDriven:.6f}')

	milesDrivenTotal = milesDrivenTotal + milesDriven
	gallonUsedTotal = gallonUsedTotal + milesPerGallon

	print('')
	milesDriven = float (input('miles driven: '))
	milesPerGallon = float (input('gallon used: '))

if milesDriven == -1 and milesPerGallon == -1:
	if milesDrivenTotal == 0 and gallonUsedTotal == 0:
			print ('Total mileage = 0')

	else:
		totalmileage = milesDrivenTotal / gallonUsedTotal
		print('')
		print(f'Total mileage = {totalmileage:.6f}')