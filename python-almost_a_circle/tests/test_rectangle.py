#!/usr/bin/python3
import unittest
import io
from unittest.mock import patch
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_area(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)

    def test_display(self):
        rect = Rectangle(3, 4)
        expected_output = "###\n###\n###\n###\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:

            rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        rect = Rectangle(3, 4, 1, 2, 99)
        self.assertEqual(str(rect), "[Rectangle] (99) 1/2 - 3/4")

    def test_update(self):
        rect = Rectangle(3, 4)
        rect.update(99, 5, 6, 7, 8)
        self.assertEqual(rect.id, 99)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 7)
        self.assertEqual(rect.y, 8)

    def test_to_dictionary(self):
        rect = Rectangle(3, 4, 1, 2, 99)
        rect_dict = rect.to_dictionary()
        expected_dict = {
            "id": 99,
            "width": 3,
            "height": 4,
            "x": 1,
            "y": 2
        }
        self.assertEqual(rect_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
