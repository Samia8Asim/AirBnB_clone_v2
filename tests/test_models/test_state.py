#!/usr/bin/python3
"""Test module for the State class"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        """Set up testing environment"""
        self.state = State()

    def tearDown(self):
        """Clean up after each test"""
        del self.state

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """Test class attributes"""
        self.assertTrue(hasattr(self.state, 'name'))

    def test_types(self):
        """Test attribute types"""
        self.assertIsInstance(self.state.name, str)

    def test_str_representation(self):
        """Test __str__ method"""
        expected_str = "[State] ({}) {}".format(self.state.id,
                                                self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method"""
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(type(state_dict['created_at']), str)
        self.assertEqual(type(state_dict['updated_at']), str)


if __name__ == '__main__':
    unittest.main()
