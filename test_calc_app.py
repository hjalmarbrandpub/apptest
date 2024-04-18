# test.py
import unittest
from app import add, subtract
"""Testing the app"""

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-2, 7), 5)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(5, -3), 8)
        self.assertEqual(subtract(0, 0), 0)

if __name__ == '__main__':
    unittest.main()