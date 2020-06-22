#---------------------------------------------------
#---------1.Entering vlue and raising error---------
def mand(a,b):
    if a in ["",'0'] or b == '0':
        print("Error")
    else:
        print("1")
a=input("Enter 1st value: ")
b=input("Enter 2st value: ")
mand(a,b)
#----------------------------------------------
#---------------2.Swapping case----------------
def swap(s):
    w=""
    for i in s:
        if i.islower():
            w+=i.upper()
        elif i.isupper():
            w+=i.lower()
        else:
            w+=i
    print("New String: ",w)
s=input("Enter a str to swap case: ")
swap(s)
#----------------------------------------------
#--------------3.abcdearian word---------------
def is_abecedarian(p):
    """Checks if the string is in alphabetical order"""
    if list(p)==sorted(p):
        print("True")
    else:
        print("False")
def remove(n):
    """Removes the special characters and returns the string."""
    w=""
    for i in n:
        if n.isalpha():
            w+=str(i)
    return w

p=remove(input("Enter a word to check if alpha order or not: "))
s=is_abecedarian(p)
#-----------------------------------------------------
#---------4. Celsius to Fahrenheit and reverese-------
def celfar(c):
    """Conversion from celsius to fahrenheit."""
    converted_f=(int(c) * 9/5)+32
    print(converted_f)

def farcel(f):
    """Conversion from fahrenheit to celsius."""
    converted_c=(int(f) - 32) * 5/9
    print(converted_c)

c=input("Enter temp in celsius: ")
celfar(c)
f=input("Enter temp in fahrenheit: ")
farcel(f)