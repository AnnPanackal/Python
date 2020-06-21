#Matrix multipliction of 3X3 matrix
def matmul(x,y):
    r=[[0,0,0],
       [0,0,0],
       [0,0,0]]
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                r[i][j]+=x[i][k]*y[k][j]
    return r
    
"""
x=[[6,8,3],
   [7,9,7],
   [3,4,5]]
y=[[4,8,5],
   [2,7,8],
   [7,1,1]]
matmul(x,y)
"""
