#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Function to test
    """
    def test_ordered_list(self):
        """ordered list"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """unordered list"""
        unordered = [1, 4, 2, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """max at the begginning"""
        max_at_beginning = [4, 3, 2, 1, -float('inf')]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """nothing"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """one elements"""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """floats max"""
        floats = [5.53, 2.6, -9.1, 15.2, 6.19]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """flaots and int max"""
        ints_and_floats = [1.53, 15.2, -9, 15, 10, float('inf')]
        self.assertEqual(max_integer(ints_and_floats), float('inf'))

    def test_string(self):
        """string"""
        string = "cramen"
        self.assertEqual(max_integer(string), 'r')

    def test_list_strings(self):
        """list string"""
        strings = ["colas", "a", "good", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """nothing string"""
        self.assertEqual(max_integer(""), None)

    def type_error(self):
        """string and int error"""
        strings = [1, 2, 3, "colas"]
        self.assertRaises(TypeError, max_integer, strings)

    def type_error(self):
        """string and int error"""
        strings = None
        self.assertRaises(TypeError, max_integer, strings)

if __name__ == '__main__':
    unittest.main()
