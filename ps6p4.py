def comp_pay_rate(job_code, hrs_worked):
    if job_code == 'L':
        pay_rate = 25
    elif job_code == 'A':
        pay_rate = 30
    elif job_code == 'J':
        pay_rate = 50

    if hrs_worked > 40:
        overtime_pay = (pay_rate * 1.5)*(hrs_worked - 40)
        regular_pay = pay_rate * 40
        gross_pay = overtime_pay + regular_pay
    else:
        gross_pay = pay_rate * hrs_worked

    return pay_rate, gross_pay

total_gross_pay = 0

response = input('Do you want to start the program (Yes or No)?')

while(response == 'Yes'):
    last_name = input('Enter last name: ')
    job_code = input('Enter job code: ')
    hrs_worked = float(input('Enter hours worked: '))
    values = comp_pay_rate(job_code, hrs_worked)
    pay_rate = values[0]
    gross_pay = values[1]
    print('Last name: ', last_name)
    print('Hours worked: ', hrs_worked)
    print('Pay rate: $%.2f'% pay_rate)
    print('Gross pay: $%.2f'% gross_pay)
    total_gross_pay = total_gross_pay + gross_pay
    response = input('Do you want to continue the program (Yes or No)?')

print('Total gross pay: $%.2f'% total_gross_pay)
