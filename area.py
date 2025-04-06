import math as m
r=float(input("Enter the radius of the circle:"))
b,h=map(float,input("Enter the base and height of the triangle respectively:").split())
l,br=map(float,input("Enter the length and breadth of the rectangle respectively:").split())

print(f'Area of circle is {round(m.pi*r**2,3)}')
print(f'Area of triangle is {0.5*b*h}')
print(f'Area of rectangle is {l*br}')


