import unittest
from zad_15 import Zespolona


class TestComplex(unittest.TestCase):

    def test_result_add(self):
        # given
        a = Zespolona(2, 3)
        b = Zespolona(3, 0)
        correct = Zespolona(5, 3)
        # when
        result = a + b
        # then
        self.assertEqual(correct, result)

    def test_result_sub(self):
        # given
        a = Zespolona(2, 6)
        b = Zespolona(2, 6)
        correct = Zespolona(0, 0)
        # when
        result = a - b
        # then
        self.assertEqual(correct, result)

    def test_result_mul(self):
        # given
        a = Zespolona(1, -5)
        b = Zespolona(3, 4)
        correct = Zespolona(23, -11)
        # when
        result = a * b
        # then
        self.assertEqual(correct, result)

    def test_result_div(self):
        # given
        a = Zespolona(2, 3)
        b = Zespolona(2, 3)
        correct = Zespolona(1, 0)
        # when
        result = a / b
        # then
        self.assertEqual(correct, result)

    def test_result_sprzezenie(self):
        # given
        a = Zespolona(2, 3)
        correct = Zespolona(2, -3)
        # when
        result = a.sprzezenie()
        # then
        self.assertEqual(correct, result)

    def test_result_modul(self):
        # given
        a = Zespolona(3, -4)
        correct = 5
        # when
        result = a.modul()
        # then
        self.assertEqual(correct, result)


if __name__ == '__main__':
    unittest.main()
