"""
Sanmple test

"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """test the calc module"""

    def test_add_number(self):
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_substract_number(self):
        """test the subtraction function"""
        res = calc.subtract(10, 5)

        self. assertEqual(res, 5)
