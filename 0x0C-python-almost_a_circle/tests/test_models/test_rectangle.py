#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        figure1 = Rectangle(15, 7)
        self.assertEqual(figure1.id, 1)
        figure2 = Rectangle(8, 18)
        self.assertEqual(figure2.id, 2)
        figure3 = Rectangle(15, 7, 1, 1, 12)
        self.assertEqual(figure3.id, 12)
        self.assertTrue(type(figure3), Rectangle)

    def test_unique_param(self):
        with self.assertRaises(TypeError):
            _ = Rectangle(1)
        _ = Rectangle(4, 4, 4, 4, 4)

    def test_yzero(self):
        figure = Rectangle(1, 2, 3, 4)
        figure.update(y=0)
        assert figure.y == 0

    def test_xzero(self):
        figure = Rectangle(1, 2, 3, 4)
        figure.update(x=0)
        assert figure.x == 0

    def test_nargs(self):
        with self.assertRaises(TypeError) as context:
            figure = Rectangle()
        self.assertFalse('required 2 arguments' in str(
            context.exception))

    def test_1_arg(self):
        with self.assertRaises(TypeError) as context:
            figure = Rectangle(5)
        self.assertFalse('required 1 argument' in str(
            context.exception))

    def test_width_negative(self):
        with self.assertRaises(ValueError) as context:
            figure = Rectangle(-3, 15)
        self.assertFalse('width positive number' in str(context.exception))

    def test_width_zero(self):
        with self.assertRaises(ValueError) as context:
            figure = Rectangle(0, 15)
        self.assertFalse('width positive number' in str(context.exception))

    def test_height_negative(self):
        with self.assertRaises(ValueError) as context:
            figure = Rectangle(8, -8)
        self.assertFalse('height positive number' in str(context.exception))

    def testheight_zero_(self):
        with self.assertRaises(ValueError) as context:
            figure = Rectangle(5, 0)
        self.assertFalse('height positive number' in str(context.exception))

    def test_area(self):
        figure = Rectangle(56, 4)
        area = figure.area()
        assert area == 224

    def test_update_width(self):
        figure = Rectangle(8, 12)
        figure.update('texto', 12)
        assert figure.id == 'texto'
        assert figure.width == 12

    def test_update_height(self):
        figure = Rectangle(8, 12)
        figure.update('texto', 8, 12)
        assert figure.id == 'texto'
        assert figure.width == 8
        assert figure.height == 12

    def test_update_kwargs_width(self):
        figure = Rectangle(8, 12)
        figure.update(width=7)
        assert figure.width == 7

    def test_update_kwargs_height(self):
        figure = Rectangle(5, 6)
        figure.update(height=10)
        assert figure.height == 10

    def test_update_kwargs_x(self):
        figure = Rectangle(5, 7)
        assert figure.x == 0
        figure.update(x=4)
        assert figure.x == 4

    def test_update_kwargs_y(self):
        figure = Rectangle(2, 4)
        assert figure.y == 0
        figure.update(y=9)
        assert figure.y == 9

    def test_update_kwargs_neg_width(self):
        with self.assertRaises(ValueError) as context:
            figure = Rectangle(5, 6)
            figure.update(width=-9)
        self.assertFalse('width positive number' in str(context.exception))

    def test_update_kwargs_zero_width(self):
        with self.assertRaises(ValueError) as context:
            figure = Rectangle(5, 6)
            figure.update(width=0)
        self.assertFalse('width positive number' in str(context.exception))

    def test_update_kwargs_nonint_width(self):
        with self.assertRaises(TypeError) as context:
            figure = Rectangle(5, 6)
            figure.update(width='text')
        self.assertFalse('width is not integer' in str(context.exception))

    def test_update_kwargs_neg_height(self):
        with self.assertRaises(ValueError) as context:
            figure = Rectangle(5, 6)
            figure.update(height=-10)
        self.assertFalse('height positive number' in str(context.exception))

    def test_update_kwargs_zero_height(self):
        with self.assertRaises(ValueError) as context:
            figure = Rectangle(5, 6)
            figure.update(height=0)
        self.assertFalse('height positive number' in str(context.exception))

    def test_update_kwargs_nonint_height(self):
        with self.assertRaises(TypeError) as context:
            figure = Rectangle(5, 6)
            figure.update(height='text')
        self.assertFalse('height is not integer' in str(context.exception))

    def test_update_kwargs_neg_x(self):
        with self.assertRaises(ValueError) as context:
            figure = Rectangle(5, 6)
            figure.update(x=-10)
        self.assertTrue('x must be >= 0' in str(context.exception))

if __name__ == '__main__':
    unittest.main()
