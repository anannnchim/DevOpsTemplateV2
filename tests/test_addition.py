import unittest
from calculator.addition import add  # Ensure correct import path


class TestAddition(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(1, 2), 3)


if __name__ == '__main__':
    unittest.main()
