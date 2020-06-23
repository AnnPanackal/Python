import unittest
import Q4June22
class check_q4(unittest.TestCase):
    def test_conpat(self):
        s='10111001111100'
        status =Q4June22.conpat(s)
        self.assertEqual(status,'11111')
    def test_conpat1(self):
        s='101001100'
        status =Q4June22.conpat(s)
        self.assertEqual(status,'11')
    
if __name__ == '__main__': 
    unittest.main() 