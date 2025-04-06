def factorial(n):
    if(n==0 or n==1):
        return 1
    elif(n<0):
        print("The number is negative")
    else:
        return n*factorial(n-1)

a=int(input("Enter a whole number:"))
result=factorial(a)
if a>0:
 print(f"The factorial of {a} is {result}")
