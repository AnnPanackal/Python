import unittest
import sqlite3
import learnConn

class test_unit(unittest.TestCase):
    def test_select(self):
        with open('C:/Users/ann/AppData/Local/Programs/Python/Python38-32/Py_Training/testing.txt','r') as d:
            obj_r=d.read()
            #print(obj_r)
        c,conn=learnConn.learn.connect(self,'C:/Users/ann/AppData/Local/Programs/Python/Python38-32/Py_Training/db_conn/connEg.db')       
        #print(c,"\n",conn)
        fn=learnConn.learn.select(self,c)
        #print(fn,"\n")
        self.assertEqual(fn,obj_r)
    
        
if __name__ == '__main__': 
    unittest.main() 
        