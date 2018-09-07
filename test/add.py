import unittest
from add import Add

class TestAdd(unittest.TestCase):
    def test_add(self):
        add = Add()
        self.assertEqual(add.add(1,2),3)


#from sample import Sample
#
#
#class TestSample(unittest.TestCase):
#    def test_calc_speed(self):
#        sample = Sample()
#        self.assertEqual(sample.calc_speed(distance=10.0, elapsed_time=2.0), 5.0)
#        self.assertEqual(sample.calc_speed(distance=10, elapsed_time=2), 5.0)
#        self.assertEqual(sample.calc_speed(distance=10, elapsed_time=4), 2.5)
#        self.assertEqual(sample.calc_speed(distance=0, elapsed_time=2), 0.0)
#
#    def test_calc_speed_invalid_value(self):
#        sample = Sample()
#
#        with self.assertRaises(ValueError):
#            sample.calc_speed(distance=10, elapsed_time=0)
#        with self.assertRaises(ValueError):
#            sample.calc_speed(distance=10, elapsed_time=-1)
#        with self.assertRaises(ValueError):
#            sample.calc_speed(distance=-10, elapsed_time=100)
#
#
#if __name__ == '__main__':
#    unittest.main()
