#-----------to print numerics in a string------------
def numprint(s):
    sl=[]
    for i in s:
        if(i.isnumeric()==True):
            sl+=i
    return sl
    