#!/usr/bin/python3
"""
unit tests for base model
"""
import unittest
import sys
from models.base import Base

class TestBase(unittest.TestCase):
    """
    unittests the base class
    """
    def test_base_repeated_id(self):
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base(7)
        b4 = Base()
        b5 = Base(7)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 7)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, 7)
