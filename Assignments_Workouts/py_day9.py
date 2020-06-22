#File Handling
"""
with open("C://Users//ann//AppData//Local//Programs//Python//Python38-32//Py_Training//day8_assignmnt_imports.py","r") as rObj:
    out=rObj.read()
    print(out)
 """  

with open("C://Users//ann//AppData//Local//Programs//Python//Python38-32//Py_Training//day8_assignmnt_def.py","r") as readObj:
    out=readObj.readlines()
    for lines in out:
        if "def" in lines:
            s=lines[3:]
            s1=s.split("(")
            print(s1[0])
