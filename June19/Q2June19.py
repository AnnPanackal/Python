#no of vowels in each words of the str
def wordvow(s):
    ns=s.split(" ")
    cs={}
    for i in ns:
        st=str(i)
        cw=0
        for k in st:
            for j in ['a','e','i','o','u']:
                if j in k:
                    cw+=1
        cs[i]=cw
    return cs
           
"""s=input("Enter str: ")
wordvow(s.lower())"""