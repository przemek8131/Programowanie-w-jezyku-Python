def iloczyn_skalarny(a: list, b: list):
    if len(a) != len(b):
        raise ValueError
    wynik = []
    for n in range(0, len(a)):
        wynik.append(a[n]*b[n])
    wynik = sum(wynik)
    return wynik


def main():
    a = [1, 2, 3, 4, 5]
    b = [9, 8, 7, 6, 5]
    print(iloczyn_skalarny(a, b))


if __name__ == '__main__':
    main()
