import numpy as np
l1=[1,2,3]
l2=[4,5,6]
a1=np.array(l1)
a2=np.array(l2)
a=a1+a2
print(a)
s=a1-a2
print(s)
d=np.dot(a1,a2)
print(d)
c=np.cross(a1,a2)
print(c)
a3=np.reshape(a2,(1,3))
print(a3)