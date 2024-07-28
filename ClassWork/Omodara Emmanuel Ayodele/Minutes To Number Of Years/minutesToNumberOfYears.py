import getnumberOf

user_Input = int(input('Enter minutes: '))
years = (getnumberOf.years_In(user_Input))
days = (getnumberOf.days_In(user_Input))
print(f"{years} years and {days:.0f} days.")




