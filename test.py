import unittest
from Shifr import Shifr

class TestShifr(unittest.TestCase):
    def setUp(self):
        self.cezare = Shifr('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG')
        self.vigener = Shifr('ATTACKATDAWN')
        self.devigener = Shifr('LXFOPVEFRNHR')
        self.vernam = Shifr('ALLSWELLTHATENDSWELL')
    def test_cezare(self):
        self.assertEqual(self.cezare.Cezare(3, 0), 'WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ')
    def test_decezare(self):
        self.assertEqual(self.cezare.Cezare(3, 1), 'QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD')
    def test_vigener(self):
        self.assertEqual(self.vigener.Viginer('LEMON', 0), 'LXFOPVEFRNHR')
    def test_devigener(self):
        self.assertEqual(self.devigener.Viginer('LEMON', 1), 'ATTACKATDAWN')
    def test_vernam(self):
        self.assertEqual(self.vernam.Vernam('LEMON', 0), 'LPH]^AHFYDM^PJP]^AHF') 
if __name__ == "__main__":
    unittest.main()
