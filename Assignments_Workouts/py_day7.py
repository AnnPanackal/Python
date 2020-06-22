"""-------------------------Using functions-----------------------------------"""
print("--------------------------Counting vowels in name---------------------------")
def vow(n,*arg):
    for i in arg:
        print(n.count(i)," is the count of",i)
    
n=input("Enter name\t")
vow(n,"a","e","i","o","u")

print("-------------------------To check for a word-----------------------------------")
def ck(s,w):
   ans=s.find(w,0,len(s))
   if ans!=-1:
    print("Present in the given str and at pos : ",ans)

s=input("Input string: ")
w=input("Enter word to be searched: ")
ck(s,w)

print("-------------------------Converting as abbrevations-------------------------")
def abbe(n):
    pos=n.split(" ")
    for i in range(len(pos)):
        if (i==0):
            print(pos[0])
        else:
            s=str(pos[i])
            print(s[0])
    
n=input("Enter name: ")
print("\nString: "+n)
abbe(n)

print("-----------------Multiplication table of 7----------------------")
def mult(m):
    print("7 * ",m," = ",7*m)

n=int(input("Enter no of multiples: "))
for i in range (n):
    mult(i+1)

print("--------------Count of Negative and Positive values------------------------")
def negpo(*args):
    n=p=0
    for i in args:
        if (i > 0):
            p+=1
        else:
            n+=1
    print("Positive: ",p)
    print("Negative: ",n)

negpo(-4,3,1,6,-7,0,-9,-1,5)




















