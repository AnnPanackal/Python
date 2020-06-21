#-----------Pattern of *----------------------
def pattern(n): 
    k = 2*n - 2
    for i in range(0, n): 
        for j in range(0, k): 
            print(end=" ") 
        k = k - 1
        for j in range(0, i+1): 
            return("* ", end="") 
        print("\n") 
        
n=int(input("Enter no of rows  "))
pattern(n)
