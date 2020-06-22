sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}
print(sampleDict)
print("---------1-------------")
sampleDict['emp4']={'name':'stella','salary':9500}
print("New dict: \n",sampleDict)
sampleDict['emp2']['salary']=10000
print("---------2-------------")
print(sampleDict)
#Marks
print("----------------------------------")
m={'stud1': {'name': 'student1', 'marks': [99, 44, 88]}, 
   'stud2': {'name': 'student2', 'marks': [88, 66, 88]}}
for i,j in m.items():
    for a,b in j.items():
        print(i,a,b)
#total marks
for i,j in m.items():
    for a,b in j.items():
        if a == 'marks':
            print("Total by: "+i+" is "+str(sum(b)))
print("----------------------------------------------")
for i,j in m.items():
    for a,b in j.items():
        print(m[i][a])
print("---------------------------------------------")
for i,j in m.items():
    for a,b in j.items():
        if isinstance(m[i][a],list):
            print(sum(m[i][a]))
#Total marks another way
for i, j in m.items():
    for a,b in j.items():
        if isinstance(m[i][a],list):
            print("Total mark scored by "+i+" is "+str(sum(m[i][a])))