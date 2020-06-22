#-------------------------------------2------------------------------

class Sep():
    def lowerFn(self,n):
        """To conver string into lowercase."""
        n=n.lower()
        print("Lower: ",n)
    def upperFn(self,n):
        """To print upper case of string."""
        print("Upper: ",n.upper())
    def splitFn(self,n):
        """To print the names splitted"""
        print("Separated names: ",n.split(" "))
    def vowelCheck(self,n):
        """To check for a vowel in the str and print the vowel"""
        ns=""
        for i in n:
            if i in ['a','e','i','o','u']:
                ns+=i
        print(set(ns)," are the vowels present in the string")
        
n=input("Enter full name: ")
obj = Sep()
obj.lowerFn(n)
obj.upperFn(n)
obj.splitFn(n)
obj.vowelCheck(n)
