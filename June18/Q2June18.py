#----Palindrome no----
def palin(s):
    ans=True
    if s==s[::-1]:
        print("Palindrome")
    else:
        ans=False
        print("Not Palindrome")
    return ans

#s=list(input("Enter a number: "))
#palin(s)