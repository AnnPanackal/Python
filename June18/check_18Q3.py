import unittest 
import Q3June18
class check_num(unittest.TestCase):
    def test_numfn(self):
        s="five"
        status = Q3June18.numfn(s)
        self.assertEqual(status,"54321")
    def test_numfn(self):
        s="eight"
        status = Q3June18.numfn(s)
        self.assertEqual(status,"8642")
        
if __name__ == '__main__': 
    unittest.main() 