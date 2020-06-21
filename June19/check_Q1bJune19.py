import unittest 
import Q1bJune19
class check_matadd(unittest.TestCase):
    def test_matadd(self):
        x=[[6,8,2],
           [7,9,2],
           [5,1,4]]
        y=[[4,8,5],
           [2,7,1],
           [3,1,8]]
        status = Q1bJune19.matadd(x,y)
        self.assertEqual(status,[[10, 16, 7], [9, 16, 3], [8, 2, 12]])
        
if __name__ == '__main__': 
    unittest.main() 