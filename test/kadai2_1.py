import unittest
from kadai2_1 import calc_price


class TestCalcPrice(unittest.TestCase):
    def test_calc_price(self):
        self.assertEqual(calc_price([10, 12]), 24)
        self.assertEqual(calc_price([40, 16]), 62)
        self.assertEqual(calc_price([100, 45]), 160)
        self.assertEqual(calc_price([50, 50, 55]), 171)
        self.assertEqual(calc_price([5]), 6)
        self.assertEqual(calc_price([]), 0)



