import unittest 
import Q1aJune19
class check_matadd(unittest.TestCase):
    def test_matadd(self):
        x=[[6,8],
           [7,9]]
        y=[[4,8],
           [2,7]]
        status = Q1aJune19.matadd(x,y)
        self.assertEqual(status,[[10, 16], [9, 16]])
        
if __name__ == '__main__': 
    unittest.main() 