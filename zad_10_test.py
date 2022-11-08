import unittest
from zad_10 import rand_liczby
from zad_10 import sortowanie


class TestSquareSolution(unittest.TestCase):

    def test_result(self):
        # given
        liczby = rand_liczby(50)
        correct = liczby
        correct.sort(reverse=True)
        # when
        result = sortowanie(liczby)
        #then
        self.assertEqual(result, correct)


    def test_empty_input(self):
        # given
        liczby = []
        correct = liczby
        correct.sort(reverse=True)
        # when
        result = sortowanie(liczby)
        # then
        self.assertEqual(result, correct)

    def test_wrong_input(self):
        liczby = ["A", "d", 1, 2]
        self.assertRaises(TypeError, sortowanie, liczby)


if __name__ == '__main__':
    unittest.main()
