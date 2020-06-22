#1.To check for a word
s="I drink coffee every morning"
print("\nString: "+s)
s1="coffee"
ans=s.find(s1,0,len(s))
if ans!=-1:
    print("coffee is present in the given str and at pos : ",ans)
#______________________________________________________________________________________________________________
#2.Alphabet after fist occourence
p="I like python ,Perl scripting"
print("\nString: "+p)
p1=p.index(",")
print("Fst alphabet after given str: "+p[p1+1])
#_______________________________________________________________________________________________________________
#3.Converting as abbrevations
n="Ann Abraham Panackal"
print("\nString: "+n)
n1=n.replace("Ann Abraham","A A")
print("Abbrevates as: "+n1)
#_______________________________________________________________________________________________________________
#4. no of white spaces
vec=": vect1 and vect2 are lists of equal length of numbers"
print("\nString: "+vec)
v=vec.count(" ",0,len(vec))
print("No of white spaces: ",v)
#______________________________________________________________________________________________________________
#5.using slicing
str1 = "PYnative"
print("\nString: "+str1)
l=len(str1)
#Yna PYnat tive PYnativ PYnativ
sans=str1[1:4]+" "+str1[:5]+" "+str1[4:]+" "+str1[:l-1]+" "+str1[:l-1]
print(sans)



