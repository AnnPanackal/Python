#1.--------------------print the pattern-------------------------
n = int(input("Enter number "))
for i in range(n, 0, -1):
    no = i
    for j in range(0, i):
        print(no, end=' ')
    print("\r")
    
    
"""
for i in [5,4,3,2,1]:
    print(str(i)*i)
"""

#2.---------number of odd and even numbers betw(533,875)-----------
print("\n\n---------------------")
odd=0
evn=0
for i in range(533,875):
    if (i%2==0):
        evn=evn+1
    else:
        odd=odd+1
print("Odd nos: ",odd)
print("Even nos : ",evn)

"""
set()
odd=l[::2]
even=set(l) - set(odd)
len(list(n))
"""
#3.--------Validity of credit card no-------------------------------
print("\n\n---------------------")
credit_lt = ['4253625879615786','4424424424442444','5122-2368-7954-3214','42536258796157867','4424444424442444','5122-2368-7954 - 3214','44244x4424442444','0525362587961578']


for no in credit_lt:
    if no.startswith('4') or no.startswith('5') or no.startswith('6'):
        if ' ' not in no and '_' not in no:
            if len(no) >= 16 and len(no) <=19 and 'x' not in no:
                #print(no)
                flag = 0
                if '-' in no:
                    split_val = no.split('-')
                    for i in split_val:
                        if len(i) !=4:
                           flag = 1
                if flag == 0:

                    skip_flag = 0
                    for j in list(range(10)):
                        #print(no,j)
                        count_val = str(no).count(str(j))
                        if count_val > 4:
                            skip_flag = 1
                            continue
                    if skip_flag ==1:
                        continue
                    print(no)

    
    

    
    


    
    

    
