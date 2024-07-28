#prompt the user to enter radius of the cylinder and store it
#prompt the user to enter length of the cylinder and store it
#given that pi is a constant which is equal to 22/7
#use the formular (pi * (radius^2)) to find the area of the cylinder and store the result of area and use the formular (area * length) to find the volume of the cylinder and store the result
#output result of area and volume

import calculator
	
radius = int (input('Enter radius: '))
length = int (input('Enter length: '))
area_result = (calculator.area(radius))
print(f'Area = {area_result:.2f}')
volume_result = (calculator.volume(radius, length))
print(f'Volume = {volume_result:.2f}')