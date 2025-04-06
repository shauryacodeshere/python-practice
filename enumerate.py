a=[12,79,100,68,'how are you?']

for i in range(0,len(a)):
    print(a[i])
    if(i==2):
        print('wow')

x=0
for j in a:
    print(j)
    if(x==2):
        print('wow')
    x+=1

for y,k in enumerate(a):
     print(k)
     if(y==2):
        print('wow')
        y+=1

for z,l in enumerate(a,start=1):
    print(l)
    if(z==2):
        print('wow')  
