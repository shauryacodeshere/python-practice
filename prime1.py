def prime(n):
    if(n==1):
         print("1 is Neither prime nor composite")
    else:
        for i in range(2,n):
            if(n%i==0):
             return False
            else:
             return True



n=int(input("Enter a number:"))
if n == 1:
    prime(n)
elif prime(n):
    print("It is prime")
else:
    print("It is not prime")
    