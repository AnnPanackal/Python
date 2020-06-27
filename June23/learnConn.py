import sqlite3

def connection():
    conn=sqlite3.connect('C:/Users/ann/Desktop/Python_Acc/Python/June23/conn.db')
    c=conn.cursor()
    return c,conn

def sqlCode(c):
    s=""
    ans=c.execute('select * from COMPANY')
    for row in ans:
        #print(row," ",type(row))
        p=[str(i) for i in row]
        t=','.join(p)
        #print(t)
        s=s+t+'\n'

    return(s)
    
if __name__=='__main__':
    c,conn=connection()
    #c.execute(f'drop table COMPANY')
    c.execute('''create table if not exists COMPANY(ID INT PRIMARY KEY NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         INT)''')
         
    with open('C:/Users/ann/Desktop/Python_Acc/Python/June23/testing.txt','r+') as filer:
        for line in filer.readlines():
            fields = line.replace('\n','').split(',')
            c.execute(f'INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)'\
      f"VALUES ('{fields[0]}','{fields[1]}','{fields[2]}','{fields[3]}','{fields[4]}')")   
    conn.commit()
    sqlCode(c)
    conn.close()