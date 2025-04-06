def Armstrong(n):
    digits = str(n)
    length=len(digits)
    ans=sum(int(digit)**length for digit in digits)
    if ans==n:
        print(f'{n} is an armstrong number')
    else:
        print(f'{n} is not an armstrong number')   

a=int(input('Enter a number:'))
Armstrong(a)