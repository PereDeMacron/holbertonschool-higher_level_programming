import unittest
from models.base import Base

class TestBaseMethods(unittest.TestCase):

    def setUp(self):
        # Set up any necessary objects or data for your tests
        pass

    def tearDown(self):
        # Clean up after each test (if necessary)
        pass

    def test_init_with_id(self):
        obj = Base(42)
        self.assertEqual(obj.id, 42)

    def test_init_without_id(self):
        obj = Base()
        self.assertTrue(hasattr(obj, 'id'))

    def test_to_json_string(self):
        data = [{'id': 1}, {'id': 2}]
        json_string = Base.to_json_string(data)
        self.assertEqual(json_string, '[{"id": 1}, {"id": 2}]')

    def test_save_to_file(self):
        data = [Base(id=1), Base(id=2)]
        Base.save_to_file(data)
        # Check if the file was created and contains the expected data

    def test_from_json_string(self):
        json_string = '[{"id": 1}, {"id": 2}]'
        data = Base.from_json_string(json_string)
        self.assertEqual(data, [{'id': 1}, {'id': 2}])

    def test_create(self):
        dictionary = {'id': 1}
        obj = Base.create(**dictionary)
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 1)

    def test_load_from_file(self):
        pass

if __name__ == '__main__':
    unittest.main()
