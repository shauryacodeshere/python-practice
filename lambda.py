'''
def cube(x):
    return x*x*x
'''

c=float(input('Enter a number:'))

cube=lambda x: x*x*x
print(f'1. {cube(c)}')

def func(x,fx):
    return x+fx(x)

print(f'2. {func(c,lambda x:x*2)}')

