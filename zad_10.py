import random
random.seed()


def rand_liczby(ilosc: int):
    liczby = []
    for i in range(0, ilosc):
        liczby.append(random.randint(0, 100))

    return liczby


def sortowanie(lista: list):

    dl = len(lista)

    while dl > 1:

        zmiana = False
        for n in range(0, dl-1):

            if lista[n] < lista[n+1]:
                lista[n], lista[n+1] = lista[n+1], lista[n]
                zmiana = True

        dl -= 1
        if zmiana is False:
            break
    return lista


def main():
    liczby = rand_liczby(50)
    print(sortowanie(liczby))


if __name__ == '__main__':
    main()
