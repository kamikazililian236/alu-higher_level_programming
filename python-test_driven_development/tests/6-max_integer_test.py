#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class containing unittest test cases for max_integer"""

    def test_max_at_end(self):
        """Test with max at the end of the list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test with max at the beginning of the list"""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_in_middle(self):
        """Test with max in the middle of the list"""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_negative(self):
        """Test with list containing one negative number"""
        self.assertEqual(max_integer([1, 2, -3, 4]), 4)

    def test_only_negative(self):
        """Test with list containing only negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_one_element(self):
        """Test list with only one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test list with float numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_ints_and_floats(self):
        """Test list with a mix of ints and floats"""
        self.assertEqual(max_integer([1, 2.5, 3]), 3)


if __name__ == '__main__':
    unittest.main()
