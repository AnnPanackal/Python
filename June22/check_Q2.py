import unittest
import Q2June22
class check_q2(unittest.TestCase):
    def test_matfn(self):
        a=[[1, 2, 3, 4],
		[7, 8, 9, 10],
		[11,12,13,14]]
        status =Q2June22.matfn(a)
        self.assertEqual(status,[[1, 2, 3, 4], [7, 13, 12, 10], [11, 8, 9, 14]])
    
    
if __name__ == '__main__': 
    unittest.main() 