#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase_init(unittest.TestCase):
    """defines unittest of the Base Class"""

    def test_no_args(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b3.id, 4)

    def test_args(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)


if __name__ == '__main__':
    unittest.main()
