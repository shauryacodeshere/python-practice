def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return round(n1/n2,2)

n1=int(input("Enter the first nummber:"))
n2=int(input("Enter the scond number:"))
print(f"The addition of two numbers are {add(n1,n2)}") 
print(f"The subtraction of two numbers are {sub(n1,n2)}") 
print(f"The multiplication of two numbers are {mul(n1,n2)}") 
print(f"The division of two numbers are {div(n1,n2)}")