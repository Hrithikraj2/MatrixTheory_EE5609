import numpy as np
# Let a=1 b=2 c=3 d=4
# Then elements of its inverse are
#     -2       1
#      1.5   -0.5
X = np.array([[1,2],[3,4]]);

Y = np.array([[-2,1],[1.5,-0.5]]);

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
   print(r)  #Identity Matrix 

