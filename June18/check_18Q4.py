import unittest 
import Q4June18
class check_bin(unittest.TestCase):
    def test_decbin(self):
        s1="10"
        s2="01"
        status = Q4June18.decbin(s1,s2)
        self.assertEqual(status,9)
    def test_decbin(self):
        s1="01"
        s2="00"
        status = Q4June18.decbin(s1,s2)
        self.assertEqual(status,4)
        
if __name__ == '__main__': 
    unittest.main() 