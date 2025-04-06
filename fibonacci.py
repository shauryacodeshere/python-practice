def f(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return f(n-1)+f(n-2)
    
a=int(input('Enter a number:'))
print(f(a))
list=[]
for i in range(0,a):
    list.append(f(i))
print(list)
