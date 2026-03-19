import unittest
from calculator import Add

class TestCalculator(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(Add(""), 0)

    def test_one_number(self):
        self.assertEqual(Add("8"), 8)
    
    def test_two_number(self):
        self.assertEqual(Add("4,9"), 13)

    def test_many_numbers(self):
        self.assertEqual(Add("1,2,9"), 12)

    def test_valueError(self):
        with self.assertRaises(ValueError):
            Add("Hello world")
    
    def test_valid_newstr(self):
        self.assertEqual(Add("1\n2,3"), 6)

    def test_invalid_newstr(self):
        with self.assertRaises(ValueError):
            Add("1,\n")
             
unittest.main(argv = ["first-arg-is-ignored"], exit = False)