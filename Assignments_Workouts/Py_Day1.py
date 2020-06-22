
a=3
b="hi"
#dir(var)->functions of the variable
print("\nThe available fns:")
print(dir(a))
print("\n")

#type(var)->
print("The type of variable:\n")
print(type(b))
print("\n")

#help(var/fn)->help info
#help(a)
#_______________________________________________________________________________________________________

#Built_In_Functions

s="hello, training is going on."
print(s)
#------------capitalize()-------------
print("\nCapitalizing 1st letter")
print(s.capitalize())
#----------center(len,'char')----------
print("\nFills the sentence with the character provided:")
t=s.center(35,'z')
print(t)
#-----------count("",0,len)------------
print("\nCounts the occourences of substring:")
print(s.count("in",0,len(s)))
#-----------find("",0,len)--------------
print("\nChecks if the str occours and returns the position in which it is present:")
print(s.find("ing",0,len(s)))
print(s.find("neat",0,len(s)))
#-----------index("",0,len)--------------------
print("\nReturns the begining index of the searched str:")
print(s.index("llo",0,10))
print(s.index("o"))
#-------------isalnum()----------------------------
print("\n true if it has a alnum otherwise false")
print(s.isalnum())
s1="Hi12what"
print(s1.isalnum())
#---------------isdigit()---------------------------
print("\nCheckes if it has digits")
print(s1.isdigit())
print(s.isdigit())
s2="1999"
print(s2.isdigit())
#---------------join(seq)---------------------------
print("\nJoins the 2 str:")
print(s1.join(s2))
#---------------lower()-------------------------------
print("\nconverts uppercase to lower")
print(s.lower())
#-----------------replace(old,new,which-one)------------
print("\nReplaces the old with the new string : ")
print(s2.replace("99","67"))

#------------------split()---------------------------
print("\nSplits the string:")
print(s.split(","))
#-----------------swapcase()----------------------
print("\nSwaps the cases of str:")
print(s.swapcase())
#-----------------strip([chars])----------------------
print("\nStrips it :")
print(t)
print(t.strip('z'))

#---------------isinstance(i,int)---------------------------------------------
#checks if it is integer or not
print(isinstance(a,int))  #true





    



