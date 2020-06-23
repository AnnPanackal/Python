def conpat(s):
    s+=str(0)
    news=n=""
    maxx=0
    for i in s:
        if(i=='1'):
            n+=str(i)
        else:
            if (len(n)>maxx):
                maxx=len(n)
                news=n
            n=""
    #print(news)
    return news

#s=input()           
#s=[1,1,1,0,1,0,1,1,1,1]
#conpat(s)