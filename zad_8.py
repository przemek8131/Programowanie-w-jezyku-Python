from pathlib import Path
from zad_7 import txt_to_string


def replacing_words(text: str):
    words = ["i", "oraz", "nigdy", "dlaczego"]
    replace_words = ["oraz", "i", "prawie nigdy", "czemu"]
    text_splitted = text.split(" ")
    assert(len(words) == len(replace_words))
    for i, w in enumerate(text_splitted):
        for j, s in enumerate(words):
            if s == w:
                text_splitted[i] = replace_words[j]

    text_splitted = " ".join(text_splitted)
    return text_splitted


def main():
    print(replacing_words(txt_to_string(Path(r'C:\Users\Przemek\Desktop\Semestr 7\Python\text_files\biology\test.txt'))))


if __name__ == '__main__':
    main()
