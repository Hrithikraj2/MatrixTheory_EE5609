import numpy as np
X = np.array([[0.314,-4.873],[4.873,0.314]]);

Y = np.array([[0.192,0.038],[-0.038,0.192]]);

# resultant matrix
result = [ [0,0],[0,0]]

my_list = []
# iterating rows of X matrix
for i in range( len(X) ):
   # iterating columns of Y matrix
   for j in range(len(Y[0])):
       # iterating rows of Y matrix
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
  

for r in result:
   print(r)