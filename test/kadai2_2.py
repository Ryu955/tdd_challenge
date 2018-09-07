import sys
import unittest
from calc_price import calc_price_side_effect
from io import StringIO

class TestPriceSideEffect(unittest.TestCase):

    test_case = """10,12
40,16
100,45

50,50,55
"""

    expects = """24
62
160
0
171
"""

    def setUp(self):
        self.inp = StringIO(self.test_case)
        self.outp = StringIO()

    def test_calc_price_side_effect(self):
        calc_price_side_effect(self.inp, self.outp)
        self.assertEqual(self.expects, self.outp.getvalue())