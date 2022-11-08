import numpy as np
from zad_12 import rand_array


def wyznacznik_macierzy(a: np.ndarray):
    m, n = a.shape
    assert(m == n)
    return np.linalg.det(a)


def main():
    ar = rand_array(5, 5)
    wyznacznik_macierzy(ar)


if __name__ == '__main__':
    main()
