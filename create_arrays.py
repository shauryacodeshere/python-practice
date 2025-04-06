import numpy as np

list=[1,23,3,4]
arr= np.array(list)
print(arr)

arr1=np.array([[1,2,3],[4,5,6],[5,6,7]])
print(arr1)
print(arr1[0,2])

arr2=np.reshape(arr1, (3,3))
print(arr2)

print(arr1[:1,:2])

