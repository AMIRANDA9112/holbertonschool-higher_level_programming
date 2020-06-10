#!/usr/bin/python3
""" Unittest """
import unittest
import json
import sys
import io

from models.base import Base

class TestBase(unittest.TestCase):
    """Tests class"""

    def setUp(self):
        """base at start point"""
        Base._Base__nb_objects = 0

    def test00(self):
        """
        this tests check that each
        class have a unique id

        base class = p0
        id = 0
        """
        p1 = Base()
        p2 = Base()
        self.assertEqual(p1.id, 1)
        self.assertEqual(p2.id, 2)

    def test01(self):
        """
        This Test check
        the correct set of id
        """
        p1 = Base(9)
        self.assertEqual(p1.id, 9)

    def test02(self):
        """
        This Test check
        the correct set of id
        """
        p1 = Base("text")
        self.assertEqual(p1.id, "text")




