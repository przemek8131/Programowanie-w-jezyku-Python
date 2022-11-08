import numpy as np
from zad_12 import rand_array


def mnozenie_macierzy(a: np.ndarray, b: np.ndarray):
    ma, na = a.shape
    mb, nb = b.shape
    if na != mb:
        raise ValueError
    wynik = np.zeros(shape=(ma, nb))
    for i in range(0, len(a)):
        for j in range(0, len(b[0])):
            for k in range(0, len(b)):
                wynik[i, j] += a[i, k] * b[k, j]

    return wynik
    # return a @ b


def main():
    a = rand_array(8, 8)
    b = rand_array(8, 8)
    print(a)
    print(b)
    print(mnozenie_macierzy(a, b))


if __name__ == '__main__':
    main()
