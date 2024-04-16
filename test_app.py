"""
Unit tests for the calculator app library
"""

import app


class TestCalculator:
    """Define tests"""
    def test_addition(self):
        """Test sum"""
        assert 4 == app.add(2, 2)

    def test_subtraction(self):
        """Test subtraction"""
        assert 2 == app.subtract(4, 2)
