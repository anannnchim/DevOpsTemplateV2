import unittest
from calculator.addition import add_number

class TestMain(unittest.TestCase):
    def test_add_number(self):
        self.assertEqual(add_number(2,1),3)
        self.assertEqual(add_number(3, 3),6)
    def test_add_number_fail(self):
        self.assertEqual(add_number(3, 4),7)



if __name__ == "__main__":
    unittest.main()


