import xml.sax

class StudentHandler(xml.sax.ContentHandler):

    def startElement(self, name, attr):
        self.current = name
        if name == "student":
            print(f"\n-- Student {attr['id']} --")

    def characters(self, content):
        if self.current == "imie":
            self.imie = content
        elif self.current == "nazwisko":
            self.nazwisko = content

    def endElement(self, name):
        if self.current == "imie":
            print(f"Imie: {self.imie}")
        elif self.current == "nazwisko":
            print(f"Nazwisko: {self.nazwisko}")
        self.current = ""


def main():
    handler = StudentHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse('source.xml')


if __name__ == '__main__':
    main()
