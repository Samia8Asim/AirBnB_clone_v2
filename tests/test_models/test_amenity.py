#!/usr/bin/python3
"""Test module for the Amenity class"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up testing environment"""
        self.amenity = Amenity()

    def tearDown(self):
        """Clean up after each test"""
        del self.amenity

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """Test class attributes"""
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_types(self):
        """Test attribute types"""
        self.assertIsInstance(self.amenity.name, str)

    def test_str_representation(self):
        """Test __str__ method"""
        expected_str = "[Amenity] ({}) {}".format(self.amenity.id,
                                                  self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method"""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(type(amenity_dict['created_at']), str)
        self.assertEqual(type(amenity_dict['updated_at']), str)


if __name__ == '__main__':
    unittest.main()
