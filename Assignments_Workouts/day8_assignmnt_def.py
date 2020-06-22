def sumDigits(s):
    tot=0
    for i in s:
        if i.isnumeric()==True:
            tot=tot+int(i)
    print("\n",tot)
def isPalindrome(s):
    if s==s[::-1]:
        print("TRUE")
    else:
        print("FALSE")
        
def ignoredcase(nw):
    w=""
    for i in nw:
        if i.isalnum()==True:
            w+=i
    return(w)
def negpo(*args):
    n=p=0
    for i in args:
        if (i > 0):
            p+=1
        else:
            n+=1
    print("Positive: ",p)
    print("Negative: ",n)
def vow(n,*arg):
    for i in arg:
        print(n.count(i)," is the count of",i)
    
def ck(s,w):
   ans=s.find(w,0,len(s))
   if ans!=-1:
    print("Present in the given str and at pos : ",ans)

def abbe(n):
    pos=n.split(" ")
    for i in range(len(pos)):
        if (i==0):
            print(pos[0])
        else:
            s=str(pos[i])
            print(s[0])
def mult(*m):
    for i in m:
        print("7 * ",i," = ",7*i)
        
def divMul(a,b):
    """ Prints the numbers divisible by 7 but not a multiple of 5."""
    for i in range (a,b):
        if (i%7==0 and i%5!=0):
            print(i,end=',')
    print("\n\n")
def liTu(*args):
    """ Prints the list and tuple of the number entered."""
    print(list(args))
    print(args)

def Fibonacci(n):
    """ Prints the fibonacci series of the term entered."""
    if n==1: 
        return 0
    elif n==2: 
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2) 


