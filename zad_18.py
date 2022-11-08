import json


class movies_json():

    def __init__(self, name):
        self.name = name
        self.dane = ""

    def save_json(self):
        with open(self.name, 'w', encoding="UTF-8") as jf:
            json.dump(self.dane, jf, ensure_ascii=False, indent=2)

    def odczytaj_json(self):
        with open(self.name, 'r', encoding="UTF-8") as jf:
            text = jf.read()
        self.dane = json.loads(text)

    def zbierz_i_dodaj_dane(self):
        tytul = input("Podaj tytuł")
        gatunek = input("Podaj gatunek")
        data = input("Podaj date premiery")
        ocena = input("Podaj ocene filmu")

        self.dane[tytul] = {'gatunek': gatunek,
                       'data': data,
                       'ocena': ocena}
        return self.dane


    def usun_dane(self):
        tytul = input("Podaj tytuł do usunięcia: ")
        del self.dane[tytul]

    def json_wypisz(self):
        json_string = json.dumps(self.dane, ensure_ascii=False, indent=2).encode("UTF-8")
        print(json_string.decode())

    def json_control(self):
        self.odczytaj_json()
        self.json_wypisz()
        i = input("Czy chcesz dodać nowe dane ? Y/N")
        if i == "Y":
            self.zbierz_i_dodaj_dane()
            i = input("Czy chcesz usunąć dane ? Y/N")
            if i == "Y":
                self.usun_dane()
        else:
            i = input("Czy chcesz usunąć dane ? Y/N")
            if i == "Y":
                self.usun_dane()
        self.save_json()


def main():
    m = movies_json('dane.json')
    m.json_control()


if __name__ == '__main__':
    main()


