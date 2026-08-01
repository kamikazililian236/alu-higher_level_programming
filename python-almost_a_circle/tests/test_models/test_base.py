#!/usr/bin/python3
"""
Unittest for Base class.
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def setUp(self):
        """Reset __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up generated files"""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_id_auto_increment(self):
        """Test default id assignment"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_explicit(self):
        """Test explicit id assignment"""
        b1 = Base(12)
        b2 = Base()
        self.assertEqual(b1.id, 12)
        self.assertEqual(b2.id, 1)

    def test_to_json_string(self):
        """Test to_json_string static method"""
        d = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        json_str = Base.to_json_string([d])
        self.assertEqual(type(json_str), str)
        self.assertTrue(len(json_str) > 0)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string(self):
        """Test from_json_string static method"""
        json_str = '[{"id": 89, "width": 10, "height": 4}]'
        list_output = Base.from_json_string(json_str)
        self.assertEqual(type(list_output), list)
        self.assertEqual(list_output[0]['id'], 89)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_save_to_file(self):
        """Test save_to_file class method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            content = f.read()
            self.assertTrue(len(content) > 0)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_create(self):
        """Test create class method"""
        r1 = Rectangle(3, 5, 1, 2, 99)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(r2.id, 99)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 2)
        self.assertIsNot(r1, r2)

    def test_load_from_file(self):
        """Test load_from_file class method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        list_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles), 1)
        self.assertEqual(list_rectangles[0].id, 1)

        # File does not exist
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        list_squares = Square.load_from_file()
        self.assertEqual(list_squares, [])


if __name__ == '__main__':
    unittest.main()
