import unittest
from validate_addr_spec import check_address
# from calc_price import calc_price_side_effect

from io import StringIO

class TestValidateAddrSpac(unittest.TestCase):

    test_cases = """abc@example.com
a..bc@example.com
"""

    expects = """ok
ng
"""

    def setUp(self):
        self.inp = StringIO(self.test_cases)
        self.outp = StringIO()

    def test_check_addr(self):
        check_address(self.inp, self.outp)
        self.assertEqual(self.expects, self.outp.getvalue())
        # self.assertEqual(True, True)
