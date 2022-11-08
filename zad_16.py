from zad_15 import Zespolona


def odczytaj_dane():
    a = input("Wprowadź pierwszą liczbę zespoloną")
    znak = input("Podaj znak działania")
    b = input("Wprowadź drugą liczbę zespoloną")
    return [a, b, znak]


def str_to_complex(com: str):
    tmp = com.split("+")
    if len(tmp) == 1:   #sprawdzenie znaku części urojonej
        tmp = com.split("-")
        im = int(tmp[1].replace("i", "")) * (-1)
    else:
        im = int(tmp[1].replace("i", ""))
    re = int(tmp[0])
    return Zespolona(re, im)

def simple_calc(rownanie: list):

    x = str_to_complex(rownanie[0])
    y = str_to_complex(rownanie[1])
    znak = rownanie[2]

    match znak:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case "/":
            return x / y


def main():
    print(simple_calc(odczytaj_dane()))


if __name__ == '__main__':
    main()
