import unittest
import Q2June17
class check_q2(unittest.TestCase):
    def test_len_str(self):
        s="mango"
        status =Q2June17.len_str(s)
        self.assertEqual(status,2)
    def test_len_str(self):
        s="pqtvdae"
        status =Q2June17.len_str(s)
        self.assertEqual(status,5)
    
if __name__ == '__main__': 
    unittest.main() 