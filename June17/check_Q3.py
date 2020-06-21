import unittest
import Q3June17
class check_q3(unittest.TestCase):
    def test_numprint(self):
        s="1ab67"
        status =Q3June17.numprint(s)
        self.assertEqual(status,['1','6','7'])
    def test_numprint(self):
        s="p9q3"
        status =Q3June17.numprint(s)
        self.assertEqual(status,['9','3'])
   
if __name__ == '__main__': 
    unittest.main() 