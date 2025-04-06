n=int(input("Enter the number of rows:"))
# half triangle
print('half triangle')

for i in range(1,n+1):
    for j in range(0,i):
        print('*',end=" ")
    i+=i    
    print('\n')

# pyramid
print('pyramid')
for i in range(1,n+1):
    for j in range(n-i,0,-1):
        print(" ",end="")       
    for k in range(0,i):
        print('*',end=' ')
   
    print()        #alternative for print('\n')  
print()
# diamond   
print('diamond')
for i in range(1,n+1):
    for j in range(n-i,0,-1):
        print(" ",end="")       
    for k in range(0,i):
        print('*',end=' ')
    print()

for i in range(n,1,-1):
    for j in range(0,n-i+1):
      print(" ",end="")
    for k in range(1,i):
        print('*',end=' ')
    print()      
