import unittest
import learnConn
import sqlite3

class test_unit(unittest.TestCase):
    def test_unit(self):
        with open('C:/Users/ann/AppData/Local/Programs/Python/Python38-32/Py_Training/testing.txt','r') as d:
            obj_r=d.read()
            #print(obj_r)
        c,conn=connectionLearn.connectt()
        #print(c,"\n",conn)
        fn=learnConn.learnInsert.sqlCode(c)
        #print(fn,"\n")
        self.assertEqual(fn,obj_r)
        
if __name__ == '__main__': 
    unittest.main() 
        