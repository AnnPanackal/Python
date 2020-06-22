#------------------Separating int,str and list------------------------------
no=[6,"A",7.9,5,3,"H",3.2,"t"]
st=[]
it=[]
ft=[]
a=b=c=0
for i in no:
    if (type(i) == str):
        st=st+list(i)
    elif (type(i) == int):
        it=it+list(str(i))
    else: 
        print(i," ")
print(st)
print(it)

#-----------------Taking input till q-----------------------------------
no=""
while(-1):
    no=input("Enter no, press q to stop\t")
    if str(no)=='q':
        exit()
    else:
        print(int(no)*int(no)*int(no))
    