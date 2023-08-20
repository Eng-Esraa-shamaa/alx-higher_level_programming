#!/usr/bin/python3
"""
unittests for square model
"""
import unittest
import io
import sys
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSquareClass(unittest.TestCase):
    """unittest square """
    def test_class_membership(self):
        """instance Square test"""
        sq = Square(1)
        self.assertIsInstance(sq, Base)
        self.assertIsInstance(sq, Rectangle)
        self.assertIsInstance(sq, Square)

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_complex_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 2, 3)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)

    def test_frozenset_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3, 1}))

    def test_range_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5))

    def test_bytes_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Python')

    def test_bytearray_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'abcdefg'))

    def test_memoryview_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'abcdefg'))

    def test_inf_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)

    def test_update_method_args_kwargs(self):
        sq11 = Square(1)
        sq11.update(1)
        self.assertEqual(sq11.__str__(), '[Square] (1) 0/0 - 1')
        sq11.update(1, 5)
        self.assertEqual(sq11.__str__(), '[Square] (1) 0/0 - 5')
        sq11.update(1, 5, 2, 3)
        self.assertEqual(sq11.__str__(), '[Square] (1) 2/3 - 5')
        sq11.update(id=99, x=4, y=7, size=8)
        self.assertEqual(sq11.__str__(), '[Square] (99) 4/7 - 8')

    def test_area_small(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_area_large(self):
        s = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s.area())

    def test_area_method(self):
        sq = Square(10)
        self.assertEqual(sq.area(), 100)

    def test_area_one_arg(self):
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1)

    @staticmethod
    def capture_stdout(sq, method):
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_size_x(self):
        s = Square(5, 5)
        correct = "[Square] ({}) 5/0 - 5".format(s.id)
        self.assertEqual(correct, s.__str__())

    def test_str_method_size_x_y(self):
        s = Square(7, 4, 22)
        correct = "[Square] ({}) 4/22 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_str_method_size_x_y_id(self):
        s = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(s))

    def test_str_method_changed_attributes(self):
        s = Square(7, 0, 0, [4])
        s.size = 15
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(s))

    def test_str_method_one_arg(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__(1)

    def test_display_one_arg(self):
        s = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            s.display(1)

    def test_update_args_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, -4)

    def test_update_args_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid")

    def test_update_args_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(98, 1, -4)

    def test_update_args_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(89, 1, 2, "invalid")

    def test_update_args_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(98, 1, 2, -4)

    def test_update_kwargs_four(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(s))

    def test_update_kwargs_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_None_id_and_more(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None, size=7, x=18)
        correct = "[Square] ({}) 18/10 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_to_dictionary_output(self):
        s = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)

    def test_update_kwargs_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)

    def test_update_kwargs_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-5)

    def test_update_args_and_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_kwargs_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_kwargs_some_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(size=5, id=89, a=1, b=54)
        self.assertEqual("[Square] (89) 10/10 - 5", str(s))

    if __name__ == '__main__':
        unittest.main()
