import unittest 
import Q1June18
class check_date(unittest.TestCase):
    def test_calcDate(self):
        s=2010
        req='min'
        status = Q1June18.calcDate(s,req)
        self.assertEqual(status,21036960)
    def test_calcDate(self):
        s=1972
        req='d'
        status = Q1June18.calcDate(s,req)
        self.assertEqual(status,731)
        
if __name__ == '__main__': 
    unittest.main() 