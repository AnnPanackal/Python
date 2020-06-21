import unittest 
import Q1cJune19
class check_matmul(unittest.TestCase):
    def test_matmul(self):
        x=[[6,8],
           [7,9]]
        y=[[4,8],
           [2,7]]
        status = Q1cJune19.matmul(x,y)
        self.assertEqual(status,[[40, 104], [46, 119]])
        
if __name__ == '__main__': 
    unittest.main() 