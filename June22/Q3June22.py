def phNo(ph):
    out=""
    s=[i for i in ph if i.isnumeric()]
    rev=ph[::-1]
    ns=[j for j in rev if j.isalpha()]
    for k in rev:  
        if k.isalpha():
            if len(s)!=10:    
                s+=k
    for i in s:           
        out+=str(i)
    #print(out)
    return out

ph="abc99ef67d8992"
#ph=input()
phNo(ph)