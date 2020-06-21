#Matrix addition of 2X2 matrix
def matadd(x,y):
    r=[[0,0],
       [0,0]]
    for i in range(len(x)):
        for j in range(len(x[0])):
            r[i][j]=x[i][j]+y[i][j]
    return(r)
'''x=[[6,8],
   [7,9]]
y=[[4,8],
   [2,7]]
matadd(x,y)'''