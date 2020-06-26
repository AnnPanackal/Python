import unittest
import learnConn
import sqlite3

class test_unit(unittest.TestCase):
    def test_unit(self):
        with open('C:/Users/ann/AppData/Local/Programs/Python/Python38-32/Py_Training/testing.txt','r') as d:
            obj_r=d.read()
            #print(obj_r)
        conn=sqlite3.connect('C:/Users/ann/AppData/Local/Programs/Python/Python38-32/Py_Training/db_conn/connEg.db')
        c=conn.cursor()
        #print(c,"\n",conn)
        fn=learnConn.sqlCode(c)
        #print(fn,"\n")
        self.assertEqual(fn,obj_r)
        
if __name__ == '__main__': 
    unittest.main() 
        