#Matrix addition of 3X3 matrix
def matadd(x,y):
    r=[[0,0,0],
       [0,0,0],
       [0,0,0]]
    for i in range(len(x)):
        for j in range(len(x[0])):
            r[i][j]=x[i][j]+y[i][j]
    return(r)
"""x=[[6,8,2],
   [7,9,2],
   [5,1,4]]
y=[[4,8,5],
   [2,7,1],
   [3,1,8]]
matadd(x,y)"""