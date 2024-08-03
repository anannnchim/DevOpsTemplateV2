import unittest
from calculator.multiply import multiplier


class TestMultiplier(unittest.TestCase):

    def test_multiplier(self):
        self.assertEqual(multiplier(2, 2), 4)


if __name__ == '__main__':
    unittest.main()
