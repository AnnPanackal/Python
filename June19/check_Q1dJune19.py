import unittest 
import Q1dJune19
class check_matmul(unittest.TestCase):
    def test_matmul(self):
        x=[[6,8,3],
           [7,9,7],
           [3,4,5]]
        y=[[4,8,5],
           [2,7,8],
           [7,1,1]]
        status = Q1dJune19.matmul(x,y)
        self.assertEqual(status,[[61, 107, 97], [95, 126, 114], [55, 57, 52]])
        
if __name__ == '__main__': 
    unittest.main() 