class Zespolona:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im >= 0:
            return "{0} + {1}i".format(self.re, self.im)
        else:
            return "{0} {1}i".format(self.re, self.im)

    def modul(self):
        return (self.re**2 + self.im**2)**(1/2)

    def sprzezenie(self):
        self.im = -self.im
        return Zespolona(self.re, self.im)

    def __add__(self, z2):
        return Zespolona(self.re + z2.re, self.im + z2.im)

    def __sub__(self, z2):
        return Zespolona(self.re - z2.re, self.im - z2.im)

    def __mul__(self, z2):
        return Zespolona(self.re * z2.re - self.im * z2.im, self.re * z2.im + self.im * z2.re)

    def __truediv__(self, z2):
        tmp = Zespolona(z2.re, z2.im)
        licznik = self * tmp.sprzezenie()
        mianownik = z2 * tmp
        return Zespolona(licznik.re/mianownik.re, licznik.im/mianownik.re)

    def __eq__(self, z2):
        if(self.re == z2.re) and (self.im == z2.im):
            return True
        else:
            return False


def main():
    a = Zespolona(1, 8)
    b = Zespolona(1, 8)
    c = a / b
    print(c)


if __name__ == '__main__':
    main()
