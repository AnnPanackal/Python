import unittest 
import add
class check_addition(unittest.TestCase):
    def test_add(self):
        n=5
        m=3
        status = add.addit(n,m)
        self.assertEqual(status,8)
    def test_add_failure(self):
        n = 5
        m = 3
        status = add.addit(n,m)
        self.assertEqual(status,53)    
        
if __name__ == '__main__': 
    unittest.main() 