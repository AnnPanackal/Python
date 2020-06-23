
def maxlist(no,n):
    a=[int(i) for i in no]
    b=[]
    for i in range(0,len(a)):
        sm=0
        cnt=[]
        for j in range(i,len(a)):
           sm=sm+a[j]
           if(sm==n):
            cnt.append(a[j])
            b.append(cnt)
            break
           elif(sm>n):
            del cnt[-1]
            sm=sm-n
           else:
            cnt.append(a[j])
    #a=[len(i) for i in b]
    return(max(b,key=len))
    
#s=['1','2','4','5','6']
#print(maxlist(s,9))
