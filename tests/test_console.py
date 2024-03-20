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


class TestConsole(unittest.TestCase):
    """test console mosule"""
    @classmethod
    def setUpCls(cls):
        """Setup the test"""
        cls.console_instance = HBNBCommand()

    @classmethod
    def tearDownCls(cls):
        """Tear down after the test"""
        del cls.console_instance

    def tDown(self):
        """Remove the temp (file.json) created during the test"""
        if (os.getenv('HBNB_TYPE_STORAGE') != 'db'):
            try:
                os.remove("file.json")
            except Exception:
                pass

    def test_console_module_has_docstrings(self):
        """Test if the console module and its methods"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)

    def test_emptyline_command(self):
        """test behavior of empty line"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console_instance.onecmd("\n")
            self.assertEqual('', mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
