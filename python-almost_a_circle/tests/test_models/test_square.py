#!/usr/bin/python3
"""
Unittest for Square class.
"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class"""

    def setUp(self):
        """Reset __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_instantiation_success(self):
        """Test successful instantiation"""
        s1 = Square(5, 1, 2, 9)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 9)

    def test_default_values(self):
        """Test instantiation with defaults"""
        s1 = Square(5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

    def test_invalid_type_size(self):
        """Test type validation for size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_invalid_value_size(self):
        """Test value validation for size"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)

    def test_size_getter_setter(self):
        """Test size getter and setter validation"""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_str(self):
        """Test __str__ representation"""
        s1 = Square(5, 2, 1, 12)
        self.assertEqual(str(s1), "[Square] (12) 2/1 - 5")

    def test_update_args(self):
        """Test update method with positional arguments"""
        s = Square(5, 1, 2, 99)
        s.update(89, 2, 3, 4)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """Test update method with keyword arguments"""
        s = Square(5, 1, 2, 99)
        s.update(x=12, size=7, y=1, id=89)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 12)
        self.assertEqual(s.y, 1)

    def test_to_dictionary(self):
        """Test to_dictionary representation"""
        s = Square(10, 2, 1, 1)
        self.assertEqual(s.to_dictionary(), {
            'id': 1, 'size': 10, 'x': 2, 'y': 1
        })


if __name__ == '__main__':
    unittest.main()
