#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(25)
        self.assertEqual(b4.id, 25)
        b5 = Base()
        self.assertEqual(b5.id, 4)
        b6 = Base()
        self.assertEqual(b6.id, Base._Base__nb_objects)

    def test_base_text(self):
        b7 = Base("texto")
        self.assertEqual(b7.id, "texto")

    def test_base_single_number(self):
        b8 = Base([5])
        self.assertEqual(b8.id, [5])

    def test_base_pair_numbers(self):
        b9 = Base({7: 7})
        self.assertEqual(b9.id, {7: 7})
        b10 = Base((9, 9))
        self.assertEqual(b10.id, (9, 9))

    def test_base_emptys(self):
        b11 = Base([])
        self.assertEqual(b11.id, [])
        b12 = Base({})
        self.assertEqual(b12.id, {})

    def test_float(self):
        b13 = Base(1.2)
        self.assertEqual(b13.id, 1.2)

    def test_NaN(self):
        b14 = Base(float("nan"))
        self.assertEqual(b14.id is float("nan"), False)

    def test_inf(self):
        b15 = Base(float("inf"))
        self.assertEqual(b15.id is float("inf"), False)

    def test_js_str_len(self):
        figure = Rectangle(25, 12, 2, 4)
        dictionary = figure.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(len(json_dictionary), len(str([{
            "x": 2, "width": 25, "id": 6, "height": 12, "y": 4}])))
        self.assertTrue(type(json_dictionary), dict)

    def test_js_str_len_sq(self):
        figure = Square(15, 2, 4, 5)
        dictionary = figure.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(len(json_dictionary), len(str([{
            "x": 2, "size": 15, "id": 5, "y": 4}])))
        self.assertTrue(type(json_dictionary), dict)

    def test_js_str_none(self):
        res = Base.to_json_string(None)
        assert res == '[]'

    def test_js_str_emty_dic(self):
        res = Base.to_json_string([{}])
        assert res == '[{}]'

    def test_json_str_emty(self):
        res = Base.to_json_string([])
        assert res == '[]'

    def test_json_str_typ(self):
        figure = Rectangle(10, 7, 2, 8)
        dictionary = figure.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(json_dictionary) is str)

    def test_save_file_len_Squ(self):
        figure1 = Square(10, 7, 2, 8)
        figure2 = Square(2, 4)
        Square.save_to_file([figure1, figure2])
        with open("Square.json") as file:
            self.assertEqual(
                    len(file.read()), len(str(
                        [{"x": 7, "id": 8, "size": 10, "y": 2}, {
                            "x": 4, "id": 7, "size": 2, "y": 0}]
                        )))

    def test_save_file_None(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), "[]")

    def test_jason_string(self):
        lists = [
            {'id': 89, 'width': 8, 'height': 3},
            {'id': 10, 'width': 3, 'height': 10}
        ]
        json_list_input = Rectangle.to_json_string(lists)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{
            'id': 89, 'width': 8, 'height': 3}, {
            'id': 10, 'width': 3, 'height': 10}])
        self.assertTrue(type(list_output), list)

if __name__ == '__main__':
    unittest.main()
