Amount_Invested = int (input ('How much would you like invest: '))

Investment_return = 0.07

amountreturnedafter10years = Amount_Invested * ( 1 + Investment_return )**10
amountreturnedafter20years = Amount_Invested * ( 1 + Investment_return )**20
amountreturnedafter30years = Amount_Invested * ( 1 + Investment_return )**30

print(f"Profit earned after 10 years-> {amountreturnedafter10years:.2f}")
print(f"Profit earned after 20 years-> {amountreturnedafter20years:.2f}")
print(f"Profit earned after 30 years-> {amountreturnedafter30years:.2f}")
