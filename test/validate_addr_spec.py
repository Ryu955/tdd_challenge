import unittest
from validate_addr_spec import check_address
from io import StringIO

class TestValidateAddrSpac(unittest.TestCase):
    def test_check_addr(self):

        with open("test3.txt", "r") as test_cases:
            with open("result3.txt", "r") as expects:

                self.inp = StringIO("".join(test_cases.readlines()))
                self.outp = StringIO()
                
                check_address(self.inp, self.outp)
                self.assertEqual("".join(expects.readlines()), self.outp.getvalue())
