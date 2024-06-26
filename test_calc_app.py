""" Test application with unittest"""
import unittest
from app import add, subtract


class TestCalculator(unittest.TestCase):
    """Testing the app"""
    def test_add(self):
        """ addition test"""
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-2, 7), 5)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        """ subtraction test"""
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(5, -3), 8)
        self.assertEqual(subtract(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
