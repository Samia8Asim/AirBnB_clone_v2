#!/usr/bin/python3
"""console.py test module"""
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models import State, Place


class TestConsoleCreate(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_state(self, mock_stdout):
        HBNBCommand().onecmd("create State name=\"California\"")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) == 36)

        state_id = output
        state = storage.all()['State.{}'.format(state_id)]
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "California")

    def test_create_place(self, mock_stdout):
        HBNBCommand().onecmd(
                "create Place city_id=\"0001\" user_id=\"0001\" name=\"My_\
                little_house\" number_rooms=4number_bathrooms=2\
                max_guest=10 price_by_night=300 latitude=37.773972\
                longitude=-122.431297"
        )
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) == 36)

        place_id = output
        place = storage.all()['Place.{}'.format(place_id)]

        self.assertIsInstance(place, Place)
        self.assertEqual(place.city_id, "0001")
        self.assertEqual(place.user_id, "0001")
        self.assertEqual(place.name, "My little house")
        self.assertEqual(place.number_rooms, 4)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 10)
        self.assertEqual(place.price_by_night, 300)
        self.assertEqual(place.latitude, 37.773972)
        self.assertEqual(place.longitude, -122.431297)


if __name__ == '__main__':
    unittest.main()
