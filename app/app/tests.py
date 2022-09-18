from django.test import TestCase

from app import calc


class CalcTests(TestCase):

    def test_add_numbers(self):
        res = calc.add(3, 7)
        self.assertEqual(res, 10)

    def test_subtract_numbers(self):
        res = calc.subtract(15, 10)

        self.assertEqual(res, 5)
