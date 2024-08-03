import unittest
from indicators.average import calculate_average


class TestAverage(unittest.TestCase):

    def test_calculate_average(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3)
        self.assertEqual(calculate_average([1]), 1)
        self.assertEqual(calculate_average([]), 0)
        self.assertEqual(calculate_average([-1, 1]), 0)


if __name__ == '__main__':
    unittest.main()
