import unittest

import numpy as np

from zad_12 import rand_array
from zad_12 import array_sum


class TestArraySum(unittest.TestCase):

    def test_result(self):
        # given
        a = rand_array(128, 128)
        b = rand_array(128, 128)
        correct = a + b
        # when
        result = array_sum(a, b)
        # then
        np.testing.assert_array_equal(result, correct)

    def test_wrong_shape(self):
        a = rand_array(128, 128)
        b = rand_array(64, 64)
        self.assertRaises(ValueError, array_sum, a, b)

    def test_wrong_input(self):
        a = [2, 1, 1, 2]
        b = [2, 3, 3, 4]
        self.assertRaises(AttributeError, array_sum, a, b)


if __name__ == '__main__':
    unittest.main()
