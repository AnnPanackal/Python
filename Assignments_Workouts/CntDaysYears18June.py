def cntLeapYear(s1,s2):
    cnt=0
    for i in range(s1,s2,1):
        if i%4==0:
            if i%100!=0:
                if i%400!=0:
                    cnt=cnt+1
    return cnt


def calcDate(s,req):
    y=s-1970
    c=cntLeapYear(1971,s+1)
    m=y*12
    d=y*365+c
    h=d*24
    min=h*60
    s=min*60
    if(req == 'y'):
        return y
    elif(req == 'm'):
        return m
    elif(req == 'd'):
        return d
    elif(req == 'h'):
        return h
    elif(req == 'min'):
        return min
    elif(req == 's'):
        return s
    else:
        return "Invalid"
    
s=int(input("Enter a year: "))
print("Enter what calculation to perform,years y,months m,days d,hours h,minutes min,seconds s")
req=input("Enter your choice: ")
out = calcDate(s,req.lower())
print(req,":",out)