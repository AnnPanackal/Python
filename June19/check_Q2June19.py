import unittest 
import Q2June19
class check_word(unittest.TestCase):
    def test_wordvow(self):
        s="hello hai wow" 
        status = Q2June19.wordvow(s)
        self.assertEqual(status,{'hello': 2, 'hai': 2, 'wow': 1})
        
if __name__ == '__main__': 
    unittest.main() 