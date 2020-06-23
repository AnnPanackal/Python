import unittest
import Q1June22
class check_q1(unittest.TestCase):
    def test_maxlist(self):
        s=['1','2','4','5','6']
        n=9
        status =Q1June22.maxlist(s,n)
        self.assertEqual(status,[1, 2, 6])
    
    
if __name__ == '__main__': 
    unittest.main() 