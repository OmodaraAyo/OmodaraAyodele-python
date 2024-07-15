print('WARNING -> Going above HRmax may lead to Cardiovascular disease.')
print ('Enter your information to know HRmax and heart rate beats per minute...\n')

name = input('What is your name: ')
age = int (input('Enter your age: '))
heartRateInBeatsPerMinute = 220 - age
heartRateRange1 = heartRateInBeatsPerMinute * 0.50
heartRateRange2 = heartRateInBeatsPerMinute * 0.85

print(f"Target heart rate: {heartRateRange1:.0f}-{heartRateRange2:.0f}(HRmax).")
print(heartRateInBeatsPerMinute, 'beats per minute.')
print(name, 'careful not to go above your Heart rate range(HRmax).')