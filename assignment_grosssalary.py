name=str(input('Enter the name of the employee:'))
bs=float(input(f'Enter the basic salary(BS) of {name}:'))
da=0.7*bs
print(f'The dearness allowance(DA) of {name} is {da}')
ta=0.3*bs
print(f'The travel allowance(TA) of {name} is {ta}')
hra=0.1*bs
print(f'The house rent allowance(HRA) of {name} is {hra}')
gross=round(bs+ta+hra,2)
print(f'The gross salary of {name} is {gross}')


