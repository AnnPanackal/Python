import unittest
import sqlite3
import learnConn

class test_unit(unittest.TestCase):
  
    def test_select(self):
        conn=sqlite3.connect('C:/Users/ann/Desktop/Python_Acc/Python/June24/connEg.db') 
        c=conn.cursor()     
        #print(c,"\n",conn)
        s=""
        ans=c.execute('select * from COMPANY')
        for row in ans:
            #print(row," ",type(row))
            p=[str(i) for i in row]
            t=','.join(p)
            #print(t)
            s=s+t+'\n'
        obj=learnConn.learn()
        fn=obj.select(c)
        #print(fn,"\n")
        self.assertEqual(fn,s)
    
    def test_insert(self):
        conn=sqlite3.connect('C:/Users/ann/Desktop/Python_Acc/Python/June24/connEg.db') 
        c=conn.cursor()
        ans=input('Enter the values ')
        obj=learnConn.learn()        
        out=obj.insert(c,conn,ans)
        self.assertEqual("Inserted successfully",out)
 
    def test_updateCode(self):
        conn=sqlite3.connect('C:/Users/ann/Desktop/Python_Acc/Python/June24/connEg.db') 
        c=conn.cursor()
        d=input('Enter values to be updated')
        du=d.split(',')
        out=learnConn.learn().updateCode(c,conn,du)
        self.assertEqual("Updated successfully",out)
       
    
        
if __name__ == '__main__': 
    unittest.main() 
        