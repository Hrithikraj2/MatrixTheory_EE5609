import numpy as np

#Let a =1 b=2 c=3 d=4
m = np.array([[1,2],[3,4]])
res =  np.linalg.inv(m)
print("Inverse of the matrix:")
print(res)