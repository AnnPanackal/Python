import unittest
import Q3June22
class check_q3(unittest.TestCase):
    def test_phNo(self):
        s="abc99ef67d8992"
        status =Q3June22.phNo(s)
        self.assertEqual(status,'99678992df')
    def test_sep(self):
        s="df93kks5r54kllg39h8k"
        status =Q3June22.phNo(s)
        self.assertEqual(status,'93554398kh')
    
if __name__ == '__main__': 
    unittest.main() 