#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Tests max_integer """

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_strings(self):
        self.assertRaises(TypeError, max_integer, ["a", "b", 1])

    def test_basic(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6]), 6)

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_basic_negative_zero(self):
        self.assertEqual(max_integer([-8, 0]), 0)

    def test_basic_negative_zero_zero(self):
        self.assertEqual(max_integer([-10, -3]), -3)

    def test_negatives(self):
        self.assertEqual(max_integer([-6, -4, 2, 6, 8, 9, 15]), 15)

    if __name__ == '__main__':
        unittest.main()
