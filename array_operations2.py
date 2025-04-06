import numpy as np
a=np.array([1,2,3])
mean=np.mean(a)
a2=np.array([4,5,6])
coeff=np.corrcoef(a,a2)
print(mean)
print(coeff)