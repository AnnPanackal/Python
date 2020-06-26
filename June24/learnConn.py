import sqlite3
import configparser
import logg_file

class learn():
    def connect(self,dbpath):
        try:
            conn=sqlite3.connect(dbpath)
            cur=conn.cursor()
            return cur,conn
        except Exception as e:
            return e
            
    def select(self,c):
        try:
            s=""
            ans=c.execute('select * from COMPANY')
            for row in ans:
                #print(row," ",type(row))
                p=[str(i) for i in row]
                t=','.join(p)
                #print(t)
                s=s+t+'\n'
                l=logg_file.logg()
                l.info("Selected")
            return(s)
        except Exception as e:
                print("Error: ",e)
    def insert(self,c,conn):
        ans=input('Enter the values ')
        anss=ans.split(',')       
        try:    
            c.execute(f'INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)'\
            f"VALUES ('{anss[0]}','{anss[1]}','{anss[2]}','{anss[3]}','{anss[4]}')")   
            conn.commit()
            l=logg_file.logg()
            l.info("Inserted")
            return("Inserted successfully")
        except Exception as e:
            print("Error: ",e)
          

    def updateCode(self,c,conn):
        try:
            d=input('Enter values to be updated')
            du=d.split(',')
            c.execute(f'UPDATE COMPANY set {du[0]} = "{du[1]}" where {du[2]}="{du[3]}"')
            conn.commit()
            l=logg_file.logg()
            l.info("Updated")
            return("Updated successfully")
        except Exception as e:
            return e
if __name__ == '__main__': 

    config=configparser.ConfigParser()
    config.read('configuration.config')
    env='DEV'
    dbpath=config.get(env,'db')
    obj=learn()
    c,conn=obj.connect(dbpath)
    #c.execute(f'drop table COMPANY')
    c.execute('''create table if not exists COMPANY(ID INT PRIMARY KEY NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         INT)''')
    """     
    with open('C:/Users/ann/AppData/Local/Programs/Python/Python38-32/Py_Training/testing.txt','r+') as filer:
        for line in filer.readlines():
            fields = line.replace('\n','').split(',')
            c.execute(f'INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)'\
      f"VALUES ('{fields[0]}','{fields[1]}','{fields[2]}','{fields[3]}','{fields[4]}')")   
    conn.commit()"""
    ch=input("1.Insert\n2.Update\n3.Select\n4.Exit\n")
    
    if ch=='1':
        c1=obj.insert(c,conn)
        print(c1)
    elif ch=='2':
        c2=obj.updateCode(c,conn)
        print(c2)
    elif ch=='3':
        c3=obj.select(c)
        print(c3)
    elif ch=='4':
        exit()
    conn.close()