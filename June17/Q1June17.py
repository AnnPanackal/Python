#-----------occourences of each char in a string------------
def sep(s):
    d={}
    occ={}
    for i in s:
        d[i]=s.count(i)
    for j,k in d.items():
        if(j==" "):
            occ["space"]=k
        else:
            occ[j]=k
    return occ
