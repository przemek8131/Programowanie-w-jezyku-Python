def pierwiastki_kw(a: float, b: float, c: float):
    delta = b**2 - 4*a*c
    if delta < 0:
        raise ValueError
    elif delta == 0:
        return -b/(2*a)
    else:
        return (-b - delta**(1/2))/(2*a), (-b + delta**(1/2))/(2*a)


def main():
    print(pierwiastki_kw(4, 10, 2))


if __name__ == '__main__':
    main()
