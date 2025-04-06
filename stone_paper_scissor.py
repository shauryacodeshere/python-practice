
import random
def check(user,comp):
    if(user==comp):
        return 0
    if(user==0 and comp==1):
        return -1
    if(user==1 and comp==2):
        return -1
    if(user==2 and comp==0):
        return -1
    if(user < 0 or user > 2 ):
        return 2
    else:
        return 1
print('\nlets play')
print('\nType 0 for stone')
print('\nType 1 for paper')
print('\nType 2 for scissors')

a=float(input("\nPlayer:"))
b=random.randint(0,2)
print(f'Computer:{b}')
score=check(a,b)

if (score==-1):
    print('\nYou lose')

if (score==0):
    print('\nIt is a draw')

if(score==1):
    print('\nYou win')

if(score==2):
    print('\nInvalid input')



