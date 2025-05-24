import unittest
from src.database.db_handler import DBHandler

class TestDBHandler(unittest.TestCase):

    def setUp(self):
        self.db_handler = DBHandler()
        self.db_handler.connect()

    def tearDown(self):
        self.db_handler.close_connection()

    def test_save_data(self):
        test_data = {
            'property_id': '123',
            'title': 'Test Property',
            'price': 250000,
            'location': 'Test Location'
        }
        result = self.db_handler.save_data(test_data)
        self.assertTrue(result)

    def test_save_data_invalid(self):
        invalid_data = {
            'property_id': None,
            'title': '',
            'price': -100,
            'location': 'Test Location'
        }
        result = self.db_handler.save_data(invalid_data)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()