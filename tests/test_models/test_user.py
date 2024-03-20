#!/usr/bin/python3
"""Test module for the User class"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up testing environment"""
        self.user = User()

    def tearDown(self):
        """Clean up after each test"""
        del self.user

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """Test class attributes"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_types(self):
        """Test attribute types"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_str_representation(self):
        """Test __str__ method"""
        expected_str = "[User] ({}) {}".format(self.user.id,
                                               self.user.__dict__)
        self.assertEqual(str(self.user), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method"""
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(type(user_dict['created_at']), str)
        self.assertEqual(type(user_dict['updated_at']), str)


if __name__ == '__main__':
    unittest.main()
