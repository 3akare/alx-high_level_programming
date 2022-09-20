#!/usr/bin/python3
"""
    unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """defines unittest for maxinteger([..])"""

    def test_maxinteger_ordered_list(self):
        """test for ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_maxinteger_unordered_list(self):
        """test for unordered list"""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_integer_reversed_list(self):
        """test for reversed list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_integer_string(self):
        """test for string"""
        self.assertEqual(max_integer("David"), 'v')

    def test_max_integer_string_list(self):
        """test for list of strings"""
        self.assertEqual(max_integer(["David", "is", "fresh"]), 'is')

    def test_max_integer_empty_list(self):
        """test for empty list"""
        self.assertEqual(max_integer([]), None)

    def test_max_integer_single_integer_list(self):
        """test for single integer list"""
        self.assertEqual(max_integer([7]), 7)

    def test_max_integer_empty_string(self):
        """test for empty string"""
        self.assertEqual(max_integer(""), None)


if __name__ == "__main__":
    unittest.main()
