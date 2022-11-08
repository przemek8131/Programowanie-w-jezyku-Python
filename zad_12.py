import numpy as np


def rand_array(a: int, b: int):
    return np.random.randint(10, size=(a, b))


def array_sum(a: np.ndarray, b: np.ndarray):
    if a.shape != b.shape:
        raise ValueError
    m, n = a.shape
    wynik = np.zeros(shape=(m, n))
    for i in range(0, m):
        for j in range(0, n):
            wynik[i, j] = a[i, j] + b[i, j]
    return wynik
    # return a + b


def main():
    a = rand_array(128, 128)
    b = rand_array(128, 128)
    array_sum(a, b)


if __name__ == '__main__':
    main()
