import unittest
import learnConn
import sqlite3

class test_connTst(unittest.TestCase):
    def test_insertion(self):
        obj=open('C:/Users/ann/AppData/Local/Programs/Python/Python38-32/Py_Training/testing.txt','r')
        obj_r=obj.read()
        conn=sqlite3.connect('C:/Users/ann/AppData/Local/Programs/Python/Python38-32/Py_Training/db_conn/connEg.db')
        c=conn.cursor()
        fn=learnConn.sqlCode(c)
        self.assertEqual(fn,obj_r)
        
    if __name__=='__main__':
        unittest.main()
        