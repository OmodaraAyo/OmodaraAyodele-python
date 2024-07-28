import poundsConverter

print('Convert from pounds to kilograms.')
user_Input = int(input('Enter value in pounds: '))
result = (poundsConverter.kilogramsOf(user_Input))
print(f'{result:.3f} kilograms')