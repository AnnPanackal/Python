#----------------------------------SUM DIGITS-----------------------------
print("-----------------------------------------------------------------------")
def sumDigits(s):
    tot=0
    for i in s:
        if i.isnumeric()==True:
            tot=tot+int(i)
    print("\n",tot)
s=input("Enter Input,will calculate digits: ")
sumDigits(s)
#-------------------------------Palindrome string--------------------------------
print("------------------------------------------")
def isPalindrome(s):
    if s==s[::-1]:
        print("TRUE")
    else:
        print("FALSE")
        
def ignoredcase(nw):
    w=""
    for i in nw:
        if i.isalnum()==True:
            w+=i
    return(w)

s=input("Enter Input to check if palindrome: ")
nw=ignoredcase(s)
isPalindrome(nw)

#-------------------------Decimal Equalent of binary no-------------------------
print("------------------------------------------")
b="-10011"
print(b," :binary")
print(int(b,2)," decimal")