import unittest 
import Q2June18
class check_palin(unittest.TestCase):
    def test_palin(self):
        s="56565"
        status = Q2June18.palin(s)
        self.assertEqual(status,True)
    def test_palin_failure(self):
        s="23"
        status = Q2June18.palin(s)
        self.assertEqual(status,False)
        
if __name__ == '__main__': 
    unittest.main() 