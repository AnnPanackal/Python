#------printing no's less than that----
def ansprint(num):
    out=""
    if(num%2==0):
        for i in range(num,0,-2):
            out=out+str(i)

    else:
        for i in range(num,0,-1):
            out=out+str(i)
    return out

def numfn(n):
    totl=["one","two","three","four","five","six","seven","eight","nine"]
    for i in range(0,len(totl)):
        if totl[i]==n:
           ans = ansprint(i+1)
           return ans
        
#n=input("Enter a number: ")
#numfn(n.lower())