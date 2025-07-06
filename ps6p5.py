def comp_tuition_owed(credit_hrs, district_code):
    if district_code == 'I':
        cost_credit = 250
    elif district_code == 'O':
        cost_credit = 550
    tuition_owed = cost_credit * credit_hrs
    return tuition_owed

total_tuition_owed = 0

response = input('Do you want to start the program (Yes or No)?')

while(response == 'Yes'):
    last_name = input('Enter last name: ')
    credit_hrs = int(input('Enter number of credit hours: '))
    district_code = input('Enter district code (I or O): ')
    tuition_owed = comp_tuition_owed(credit_hrs, district_code)
    print('Last name: ', last_name)
    print('Tuition owed: $%.2f'% tuition_owed)
    total_tuition_owed = total_tuition_owed + tuition_owed
    response = input('Do you want to continue this program (Yes or No)?')

print('Total tuition owed: $%.2f'% total_tuition_owed)