#!/usr/bin/python3
"""console.py test module"""
import unittest
from unittest.mock import patch
from console import HBNBCommand
import os
from models import storage
from models.city import City
from models.user import User
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def test_db_create_city(self):
        """Test creating a City instance with DBStorage."""
        with patch('sys.stdout', new=StringIO()) as cout:
            HBNBCommand().onecmd('create City name="Paris" state_id="123"')
            output = cout.getvalue().strip()
            self.assertTrue(len(output) == 36)

            city_id = output
            city = storage.get(City, city_id)

            self.assertIsInstance(city, City)
            self.assertEqual(city.name, "Paris")
            self.assertEqual(city.state_id, "123")

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def test_db_create_user(self):
        """Test creating a User instance with DBStorage."""
        with patch('sys.stdout', new=StringIO()) as cout:
            HBNBCommand().onecmd(
                    'create User email="test@example.com"\
                    password="password123"'
            )
            output = cout.getvalue().strip()
            self.assertTrue(len(output) == 36)

            user_id = output
            user = storage.get(User, user_id)

            self.assertIsInstance(user, User)
            self.assertEqual(user.email, "test@example.com")
            self.assertEqual(user.password, "password123")


if __name__ == '__main__':
    unittest.main()
