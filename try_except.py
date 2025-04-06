try:
    a=input('enter a number:')
    for i in range(1,11):
        print(f'Multiplication table of {a} is {int(a)*i} ')

except ValueError:
    print('It is not an integer')
