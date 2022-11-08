from pathlib import Path


def ile(p: Path, a: bool):
    p = Path(p)
    ilosc = 0
    if p.is_dir():
        for x in p.iterdir():
            if x.is_dir():
                ilosc += ile(x, a)
            else:
                ilosc += 1
                if a:
                    print(x)
    return ilosc


if __name__ == '__main__':
    print(ile(Path('C:\OrCAD'), False))
