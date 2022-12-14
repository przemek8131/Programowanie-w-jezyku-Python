from pathlib import Path


def txt_to_string(p: Path):
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def cutting_words(text: str):
    words = ["się", "i", "oraz", "nigdy", "dlaczego"]
    text_splitted = text.split(" ")
    for i, w in enumerate(text_splitted):
        for s in words:
            if s == w:
                del text_splitted[i]
                i -= 1

    text_splitted = " ".join(text_splitted)
    return text_splitted


def main():
    print(cutting_words(txt_to_string(Path(r'C:\Users\Przemek\Desktop\Semestr 7\Python\text_files\biology\test.txt'))))


if __name__ == '__main__':
    main()
