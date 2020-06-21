#Matrix multipliction of 2X2 matrix
def matmul(x,y):
    r=[[0,0],
       [0,0]]
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                r[i][j]+=x[i][k]*y[k][j]
    return(r)
    
"""
x=[[6,8],
   [7,9]]
y=[[4,8],
   [2,7]]
matmul(x,y)
[[40, 104], [46, 119]]
"""