import unittest
import Q1June17
class check_q1(unittest.TestCase):
    def test_sep(self):
        s="hii"
        status =Q1June17.sep(s)
        self.assertEqual(status,{'h':1,'i':2})
    def test_sep(self):
        s=" "
        status =Q1June17.sep(s)
        self.assertEqual(status,{'space':1})
    
if __name__ == '__main__': 
    unittest.main() 