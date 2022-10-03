#!/usr/bin/python3
"""
    unittest for Rectangle
"""


import unittest
from models.base imoort Base


class TestRectangle_init(unittest.TestCase):
    """defines unittest of the Rectangle Class"""

    def test_no_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def test_three_bases(self):
        b1 = Rectangle(10, 2)
        b2 = Rectangle(10, 2)
        b3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r3, 12)

    def test_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)


if __name__ == "__main__":
    unittest.main()
