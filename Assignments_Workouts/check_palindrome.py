
import unittest 
import palin
class check_palindrome(unittest.TestCase):
    def test_palin(self):
        str1 = 'malayalam'
        status = palin.check_palin(str1)
        self.assertEqual(status,True)
    def test_palin_failure(self):
        str1 = 'mal'
        status = palin.check_palin(str1)
        self.assertEqual(status,False)    
        
if __name__ == '__main__': 
    unittest.main() 
