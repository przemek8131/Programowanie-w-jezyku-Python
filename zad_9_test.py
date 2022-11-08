import unittest
from zad_9 import pierwiastki_kw


class TestSquareSolution(unittest.TestCase):

    def test_no_solution(self):
        self.assertRaises(ValueError, pierwiastki_kw, 1, 1, 1)

    def test_one_solution(self):
        # given
        a = 1
        b = 2
        c = 1
        correct = -1
        # when
        result = pierwiastki_kw(a, b, c)
        # then
        self.assertEqual(result, correct)

    def test_two_solution(self):
        # given
        a = 1
        b = 5
        c = 6
        correct = (-3.0, -2.0)
        # when
        result = pierwiastki_kw(a, b, c)
        # then
        self.assertEqual(result, correct)

    def test_missing_argument(self):
        self.assertRaises(TypeError, pierwiastki_kw, 1, 2)

    def test_wrong_input(self):
        self.assertRaises(TypeError, pierwiastki_kw, 1, "sd", 23)


if __name__ == '__main__':
    unittest.main()
