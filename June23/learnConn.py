import sqlite3

def connection():
    conn=sqlite3.connect('C:/Users/ann/AppData/Local/Programs/Python/Python38-32/Py_Training/db_conn/connEg.db')
    c=conn.cursor()
    return c,conn

def sqlCode(c):
    s=""
    ans=c.execute("select * from COMPANY")
    for row in ans:
        #p=','.join(row)
        s='\n'
    return(s)
    
if __name__=='__main__':
    c,conn=connection()
    c.execute('delete from COMPANY')
    c.execute('''create table if not exists COMPANY(ID INT PRIMARY KEY NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL)''')
         
    with open('C:/Users/ann/AppData/Local/Programs/Python/Python38-32/Py_Training/testing.txt','r+') as filer:
        for line in filer.readlines():
            fields = line.replace('\n','').split(',')
            c.execute(f'INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)'\
      f"VALUES ('{fields[0]}','{fields[1]}','{fields[2]}','{fields[3]}','{fields[4]}')")   
    conn.commit()
    sqlCode(c)
    conn.close()