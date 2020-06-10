#!/usr/bin/python3
""" Unittest """
import unittest
import json
import sys
import io

from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Tests class"""

    def test_00_id(self):
        """ Correct Case id: full args """
        self.assertEqual(Rectangle(1, 2, 3, 4, 5).id, 5)


