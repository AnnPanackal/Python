#mul by 50 and div by 100
li=[1,2,3,4,5,6,7,8,9,10]
c=[]
for i in li:
    c.append(i*10)
    #print("\tin loop\t",c)
print(c)

final=[]
for j in c:
    if j%50==0:
        final.append(j)
print(final)