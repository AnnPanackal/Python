def matfn(a):
    p=[[0,0,0],
       [0,0,0],
       [0,0,0]]
    for i in range(3):
        for j in range(4):
            if i==1 and j==1:
                p[i][j]=a[i][j]
                a[i][j]=a[i+1][j+1]
 
                p[i][j+1]=a[i][j+1]
                a[i][j+1]=a[i+1][j]
  
                p[i+1][j]=a[i+1][j]
                a[i+1][j]=p[i][j]
           
                p[i+1][j+1]=a[i+1][j+1]
                a[i+1][j+1]=p[i][j+1]
    #print(a) 
    return a
            
"""
a=[[1, 2, 3, 4],
   [7, 8, 9, 10],
   [11,12,13,14]]
matfn(a)
"""