
import numpy as np
a=np.array([[1,2,3],
           [3,4,5],
           [5,6,7]])
b=np.array([[6,7,8],
           [6,8,9],
           [9,1,5]])
print (a*b)




#programme without numpy
x = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
y = [[10, 11, 12],
     [14, 15, 16],
     [18, 19, 20]]
r = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

for i in range(len(x)):
    for j in range(len(y[0])):
		for k in range(len(y)):
                       #have a doubt in this expression
			r[i][j] = r[i][j] + x[i][k] * y[k][j]

			
for m in r:
    print(m)
