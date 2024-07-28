import calculator_calculate

name = input('Enter your name: ')
hours_Worked = int (input('Enter number of hours worked this week: '))
hourly_pay_rate = float (input('Enter hourly pay rate: $'))
federal_Tax_Rate = float (input('Enter federal tax withholding rate: '))
state_Tax_Rate = float (input('Enter state tax withholding rate: '))
grossPay = (calculator_calculate.gross_pay(hours_Worked, hourly_pay_rate))
federal_Withholding_tax_rate =  (calculator_calculate.federal_withholding(hours_Worked, hourly_pay_rate))
state_withholding_tax_rate = (calculator_calculate.state_withholding(hours_Worked, hourly_pay_rate))
total_deduction = federal_Withholding_tax_rate + state_withholding_tax_rate
net_pay = grossPay - total_deduction

print()
print(f'Employee name -> {name}')
print(f'Hours Worked: {hours_Worked}')
print(f'Pay Rate: ${hourly_pay_rate}')
print(f'Gross Pay: ${grossPay}') 
print(f'Federal Tax Rate -> ${federal_Withholding_tax_rate}')
print(f'State Tax Rate -> ${state_withholding_tax_rate:.2f}')
print(f'Total deduction: ${total_deduction:.2f}')
print(f'Net Pay: ${net_pay:.2f}')
