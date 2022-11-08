import xml.dom.minidom


def main():
    domtree = xml.dom.minidom.parse('source.xml')
    osoby = domtree.documentElement
    studenci = osoby.getElementsByTagName('student')

    for student in studenci:
        print(f"\n-- Student {student.getAttribute('id')} --")

        imie = student.getElementsByTagName('imie')[0].childNodes[0].nodeValue
        nazwisko = student.getElementsByTagName('nazwisko')[0].childNodes[0].nodeValue

        print(f"Imie: {imie}")
        print(f"Nazwisko: {nazwisko}")

    studenci[1].getElementsByTagName('imie')[0].childNodes[0].nodeValue = "Jacek"

    with open('source.xml', 'w', encoding="UTF-8") as fp:
        domtree.writexml(fp)


if __name__ == '__main__':
    main()
