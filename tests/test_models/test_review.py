#!/usr/bin/python3
"""Test module for the Review class"""

import unittest
from models.review import Review
from models.place import Place
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def setUp(self):
        """Set up testing environment"""
        self.review = Review()

    def tearDown(self):
        """Clean up after each test"""
        del self.review

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        """Test class attributes"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_types(self):
        """Test attribute types"""
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_str_representation(self):
        """Test __str__ method"""
        expected_str = "[Review] ({}) {}".format(self.review.id,
                                                 self.review.__dict__)
        self.assertEqual(str(self.review), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method"""
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(type(review_dict['created_at']), str)
        self.assertEqual(type(review_dict['updated_at']), str)

    def test_place_relationship(self):
        """Test place relationship"""
        place = Place()
        self.review.place_id = place.id
        self.assertEqual(self.review.place_id, place.id)
        self.assertIsInstance(self.review.place_id, str)

    def test_user_relationship(self):
        """Test user relationship"""
        user = User()
        self.review.user_id = user.id
        self.assertEqual(self.review.user_id, user.id)
        self.assertIsInstance(self.review.user_id, str)


if __name__ == '__main__':
    unittest.main()
