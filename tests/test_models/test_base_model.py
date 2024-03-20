#!/usr/bin/python3
"""Testing file for the BaseModel"""

import unittest
import datetime
import json
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Class for testing the BaseModel"""

    def setUp(self):
        """Set up for testing"""
        self.name = 'BaseModel'
        self.value = BaseModel()
        self.value.save()

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """Test default instantiation"""
        i = self.value
        self.assertEqual(type(i), BaseModel)

    def test_kwargs(self):
        """Test instantiation with kwargs"""
        i = self.value
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertNotEqual(new, i)

    def test_kwargs_int(self):
        """Test instantiation with kwargs containing int"""
        i = self.value
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Test save method"""
        i = self.value
        i.save()
        key = '{}.{}'.format(self.name, i.id)
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test __str__ method"""
        i = self.value
        expected_str = '[{}] ({}) {}'.format(self.name, i.id, i.__dict__)
        self.assertEqual(str(i), expected_str)

    def test_to_dict(self):
        """Test to_dict method"""
        i = self.value
        self.assertEqual(i.to_dict(), i.__dict__)

    def test_kwargs_none(self):
        """Test instantiation with kwargs containing None"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = BaseModel(**n)

    def test_kwargs_one(self):
        """Test instantiation with kwargs containing one non-recognized key"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = BaseModel(**n)

    def test_id(self):
        """Test id attribute"""
        new = BaseModel()
        self.assertIsInstance(new.id, str)

    def test_created_at(self):
        """Test created_at attribute"""
        new = BaseModel()
        self.assertIsInstance(new.created_at, datetime.datetime)

    def test_updated_at(self):
        """Test updated_at attribute"""
        new = BaseModel()
        self.assertIsInstance(new.updated_at, datetime.datetime)
        self.assertNotEqual(new.created_at, new.updated_at)


if __name__ == '__main__':
    unittest.main()
