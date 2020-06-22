#-------------------------------------1------------------------------
class srt():
    try:
        def is_sorted(self,n):
            for i in range(0,len(n)-1):
                if(n[i]>n[i+1]):
                    print("False")
                    exit()
            print("True")
    except Exception as e:
        print("Error: ",e)
n=input("Enter a list: ")
obj=srt()
obj.is_sorted(n)
    
