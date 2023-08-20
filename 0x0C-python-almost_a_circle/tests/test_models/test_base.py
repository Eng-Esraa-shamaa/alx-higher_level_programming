#!/usr/bin/python3
"""
unit tests for base model
"""
import unittest
import sys
import json
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_base_types(self):
        """Base types test"""
        Base._Base__nb_objects = 0
        self.assertEqual(str(type(Base)), "<class 'type'>")

        self.assertEqual(str(type(Rectangle)), "<class 'type'>")

        self.assertEqual(str(type(Square)), "<class 'type'>")

    def test_instance_Rectangle(self):
        """ instance tests"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 4)
        self.assertEqual(isinstance(r1, Rectangle), True)

    def test_instance_Square(self):
        """instance tests"""
        Base._Base__nb_objects = 0
        sq1 = Square(4)
        self.assertEqual(isinstance(sq1, Square), True)

    def test_type_instance_rectangle(self):
        """same type test"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(1, 2)
        self.assertEqual(str(type(r1)), "<class 'models.rectangle.Rectangle'>")

    def test_type_instance_square(self):
        """same types test"""
        Base._Base__nb_objects = 0
        sq1 = Square(2)
        self.assertEqual(str(type(sq1)), "<class 'models.square.Square'>")

    def test_subclass(self):
        """test if they are subclasses"""
        Base._Base__nb_objects = 0
        self.assertEqual(issubclass(Square, Rectangle), True)
        self.assertEqual(issubclass(Square, Base), True)
        self.assertEqual(issubclass(Rectangle, Base), True)

        self.assertEqual(issubclass(Base, Rectangle), False)
        self.assertEqual(issubclass(Base, Square), False)

    def test_Equal_rectangle(self):
        """test if they are equal"""
        Base._Base__nb_objects = 0
        r2 = Rectangle(4, 5)
        r3 = Rectangle(4, 5)
        self.assertEqual(r2 is r3, False)

    def test_Equal_square(self):
        """test if they are equal"""
        Base._Base__nb_objects = 0
        sq2 = Square(4)
        sq3 = Square(4)
        self.assertEqual(sq2 is sq3, False)

    def test_None_base(self):
        """test id the base empty"""
        Base._Base__nb_objects = 0
        base1 = Base(None)
        self.assertEqual(base1.id, 1)

    def test_more_args_base(self):
        """test if the base with more args"""
        with self.assertRaises(TypeError):
            base1 = Base(1, 2)

    def test1_to_json_string(self):
        """test case to JSON string"""
        Base._Base__nb_objects = 0
        rect = Rectangle(5, 4, 3, 6)
        new_dict = rect.to_dictionary()
        jstrg = Base.to_json_string([new_dict])
        self.assertEqual(new_dict, {'y': 6, 'height': 4,
                                    'width': 5, 'x': 3, 'id': 1})
        self.assertEqual(type(new_dict), dict)
        self.assertEqual(sorted(jstrg),
                         sorted('[{"height": 4, "x": 3, "width": '
                                '5, "y": 6, "id": 1}]'))

    def test2_to_json_string_type(self):
        """test when passing to JSON string"""
        Base._Base__nb_objects = 0
        rect = Rectangle(5, 4, 3, 6)
        new_dict = rect.to_dictionary()
        jstrg = Base.to_json_string([new_dict])
        self.assertEqual(type(jstrg), str)

    def test3_to_json_string(self):
        """test when pass to JSON string"""
        Base._Base__nb_objects = 0
        new_dict = None
        jstrg = Base.to_json_string([new_dict])
        self.assertEqual(jstrg, '[null]')

    def test4_to_json_string(self):
        """test when pasin JSON string"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test5_to_json_string(self):
        """funct when pass to JSON string"""
        Base._Base__nb_objects = 0
        jstrg = Base.to_json_string([])
        self.assertEqual(jstrg, "[]")

    def test6_to_json_string(self):
        """pass to JSON string"""
        Base._Base__nb_objects = 0
        MyList = [1, 2, 3]
        jstrg = Base.to_json_string([MyList])
        self.assertEqual(jstrg, "[[1, 2, 3]]")

    def test1_json_to_file1(self):
        """ test the json string to file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 4)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        lista = [{"id": 1, "width": 2, "y": 0, "x": 0, "height": 4},
                 {"id": 2, "width": 2, "y": 0, "x": 0, "height": 4}]
        with open("Rectangle.json", "r") as file:
            file1 = file.read()
            list_output = Rectangle.from_json_string(file1)
            self.assertEqual(list_output, lista)

    def test7_json_to_file7(self):
        """ test json str to file"""
        Base._Base__nb_objects = 0
        with self.assertRaises(AttributeError):
            MyList = ["hello", "my", "friend"]
            Square.save_to_file(MyList)

    def test8_json_to_file8(self):
        """ test to json str into file"""
        Base._Base__nb_objects = 0
        with self.assertRaises(AttributeError):
            Square.save_to_file([None])

    def test9_json_to_file9(self):
        """ test to json string into file"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test0_json_str_to_dic(self):
        """test json str to dictionary"""
        Base._Base__nb_objects = 0
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10,
                                        'id': 89}, {'height': 7, 'width': 1,
                                                    'id': 7}])

    def test_display_1(self):
        """test display 1"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 3)
        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        r1.display()
        self.assertEqual(captureOutput.getvalue(), ("##\n##\n##\n"))

    def test_display_2(self):
        """test display 1"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            """ test display 2 """
            r2 = Rectangle()
            captureOutput = io.StringIO()
            sys.stdout = captureOutput
            r2.display()


if __name__ == "__main__":
    unittest.main()
