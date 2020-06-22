"""
a=5
b=10
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
"""
def up(n):
    u=0
    for i in n:
        if i.isupper()==True:
            u+=1
    print("Upper: ",u)
def low(n):
    l=0
    for i in n:
        if i.islower()==True:
            l+=1
    print("Lower: ",l)