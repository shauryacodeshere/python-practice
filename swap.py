n1=float(input("Enter n1:"))
n2=float(input("Enter n2:"))

def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

print(f'before swapping:n1={n1} & n2={n2}')
print(f'after swapping:{swap(n1,n2)}')
