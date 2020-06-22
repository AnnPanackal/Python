info = {'sakthi':{'class' :11,'subject':{'science':99, 'maths':70,'social':80}},
        'alia'  :{'class' :10,'subject':{'science':92, 'maths':84,'social':78}},
        'teena' :{'class' :8 ,'subject':{'science':95, 'maths':81,'social':97}},
        'elle'  :{'class' :12,'subject':{'science':76, 'maths':67,'social':99}},
        'priya' :{'class' :5 ,'subject':{'science':91, 'maths':93,'social':90}}}
"""
print("Avg scores are :")
name=s=""
for i,j in info.items():
    for a,b in j.items():
        if a == 'subject':
            avg = (b['science']+b['maths']+b['social'])/3
            print(i+"\t:\t",avg)
            s=s+str(int(avg))+" "
            name=name+str(i)+" "
s=s.split(" ")
name=name.split(" ")
pos=s.index(max(s))
print("Student with highest mark is: ",name[pos])
"""
d={}
for i,j in info.items():
    for a,b in j.items():
        if(isinstance(b,dict)):
            c=b.values()
            d[i]=sum(c)/3
print(d)
print(max(d,key=d.get))

