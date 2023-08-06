#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_no_args(self):
        """test no arguments"""
        self.assertIsNone(max_integer())

    def test_emptylist(self):
        """test an empty list []"""
        test = []
        self.assertIsNone(max_integer(test))

    def test_max_in_begginning(self):
        """test beginning """
        max_in_beginning = [8, 5, 3, 1]
        self.assertEqual(max_integer(max_in_beginning), 8)

    def test_all_negative(self):
        """test all negative numbers"""
        test_negative = [-1, -20, -3, -15, -5]
        self.assertEqual(max_integer(test_negative), -1)

    def test_floats(self):
        """Test a list of float numbers."""
        floats = [4.53, 6.3, -8.8, 17.6, 8.0]
        self.assertEqual(max_integer(floats), 17.6)

    def test_one_element_list(self):
        """Test a list with only one element."""
        one_element = [8]
        self.assertEqual(max_integer(one_element), 8)

    def test_one_negative(self):
        """test negative number in the list"""
        test = [10, -10, 1, 8, 7, 2]
        self.assertEqual(max_integer(test), 10)

    def test_all_10(self):
        """test all numbers are 10 """
        test = [10, 10, 10, 10, 10, 10]
        self.assertEqual(max_integer(test), 10)

    def test_max_at_middle(self):
        """test max number in middle"""
        test_max = [1, 10, 23, 40, 4, 17]
        self.assertEqual(max_integer(test_max), 40)

    def test_non_int_arg(self):
        """Check: non integer type"""
        test = [1, "string", 8, 4, 5]
        with self.assertRaises(TypeError):
            max_integer(test)


if __name__ == "__main__":
    unittest.main()
