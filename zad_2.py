def main():
    dane = input("Podaj imie, nazwisko i date urodzenia")
    [imie, nazwisko, data] = dane.split(" ")
    print(imie)
    print(nazwisko)
    print(data)


if __name__ == '__main__':
    main()
