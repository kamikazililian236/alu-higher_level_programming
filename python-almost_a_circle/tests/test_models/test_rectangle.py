#!/usr/bin/python3
"""
Unittest for Rectangle class.
"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def setUp(self):
        """Reset __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_instantiation_success(self):
        """Test successful instantiation"""
        r1 = Rectangle(10, 2, 1, 3, 9)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 9)

    def test_default_values(self):
        """Test instantiation with defaults"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_invalid_type_width(self):
        """Test type validation for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_invalid_value_width(self):
        """Test value validation for width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 2)

    def test_invalid_type_height(self):
        """Test type validation for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, [2])

    def test_invalid_value_height(self):
        """Test value validation for height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_invalid_type_x(self):
        """Test type validation for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "1")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, None)

    def test_invalid_value_x(self):
        """Test value validation for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1)

    def test_invalid_type_y(self):
        """Test type validation for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, "1")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, {})

    def test_invalid_value_y(self):
        """Test value validation for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 0, -1)

    def test_area(self):
        """Test area calculation"""
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.area(), 12)

    def test_str(self):
        """Test __str__ representation"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_without_xy(self):
        """Test display method without x and y coordinates"""
        r = Rectangle(2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_with_xy(self):
        """Test display method with x and y coordinates"""
        r = Rectangle(2, 2, 1, 1)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n ##\n ##\n")

    def test_update_args(self):
        """Test update method with positional arguments"""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        """Test update method with keyword arguments"""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(id=89, width=2, height=3, x=4, y=5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_to_dictionary(self):
        """Test to_dictionary representation"""
        r = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(r.to_dictionary(), {
            'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9
        })


if __name__ == '__main__':
    unittest.main()
