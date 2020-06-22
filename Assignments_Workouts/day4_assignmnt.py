#------------Multiplication table of 7------------------------------------
m=int(input("Enter no of multiples of 7 you want\t"))
for i in range(1,m+1):
     print(7*i)

#--------------Count of Negative and Positive values-------------------------
np=[-4,3,1,6,-7,0,-9,-1,5]
print(np)
p=n=0
for i in np:
    if (i>0):
        p+=1
    else:
        n+=1
print("Positive: ",p,"\nNegative: ",n)