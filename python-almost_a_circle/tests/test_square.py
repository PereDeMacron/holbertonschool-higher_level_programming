import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_attributes(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_str_method(self):
        square = Square(4, 1, 1, 2)
        self.assertEqual(str(square), "[Square] (2) 1/1 - 4")

    def test_update_method(self):
        square = Square(3, 2, 2, 1)
        square.update(4, 5, 6, 7)
        self.assertEqual(square.id, 4)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 7)

    def test_to_dictionary_method(self):
        square = Square(3, 2, 2, 1)
        square_dict = square.to_dictionary()
        expected_dict = {
            "id": 1,
            "size": 3,
            "x": 2,
            "y": 2
        }
        self.assertEqual(square_dict, expected_dict)

if __name__ == "__main__":
    unittest.main()
