def code():
     for i in range(0,len(a)):
        a[i]=a[len(a)-1-i]
        for j in range(0,len(a[i])):
             a[i][j]=a[i][len(a[i])-1-j]


a=str(input('Enter a string:'))
code()


    
