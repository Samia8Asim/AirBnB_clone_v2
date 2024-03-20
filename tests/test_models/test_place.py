#!/usr/bin/python3
"""Test module for the Place class"""

import unittest
from models.place import Place
from models.city import City
from models.user import User
from models.state import State
from models.base_model import BaseModel
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def setUp(self):
        """Set up testing environment"""
        self.place = Place()

    def tearDown(self):
        """Clean up after each test"""
        del self.place

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """Test class attributes"""
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_types(self):
        """Test attribute types"""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_str_representation(self):
        """Test __str__ method"""
        expected_str = "[Place] ({}) {}".format(self.place.id,
                                                self.place.__dict__)
        self.assertEqual(str(self.place), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method"""
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(type(place_dict['created_at']), str)
        self.assertEqual(type(place_dict['updated_at']), str)

    def test_save_method(self):
        """Test save method"""
        prev_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(prev_updated_at, self.place.updated_at)

    def test_state_relationship(self):
        """Test state relationship"""
        state = State()
        self.place.state_id = state.id
        self.assertEqual(self.place.state_id, state.id)
        self.assertIsInstance(self.place.state_id, str)

    def test_city_relationship(self):
        """Test city relationship"""
        city = City()
        self.place.city_id = city.id
        self.assertEqual(self.place.city_id, city.id)
        self.assertIsInstance(self.place.city_id, str)

    def test_user_relationship(self):
        """Test user relationship"""
        user = User()
        self.place.user_id = user.id
        self.assertEqual(self.place.user_id, user.id)
        self.assertIsInstance(self.place.user_id, str)


if __name__ == '__main__':
    unittest.main()
