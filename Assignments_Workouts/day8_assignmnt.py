#----------------------------1---------------------------------------
def divMul(a,b):
    """ Prints the numbers divisible by 7 but not a multiple of 5."""
    for i in range (a,b):
        if (i%7==0 and i%5!=0):
            print(i,end=',')
print(divMul.__doc__)
divMul(5000,7500)

#---------------------------2---------------------------------------------
def liTu(*args):
    """ Prints the list and tuple of the number entered."""
    print(list(args))
    print(args)
print(liTu.__doc__) 
liTu(input("Enter nos: "))

#-------------------------------3---------------------------------------
def Fibonacci(n):
    """ Prints the fibonacci series of the term entered."""
    if n==1: 
        return 0
    elif n==2: 
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2) 
sprint(Fibonacci.__doc__)
if no>200 or no<0:
    print("Invalid no")
    exit()
for i in range(1,no):
    print(Fibonacci(i)) 

