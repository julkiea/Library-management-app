class Reader:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number

    def create_reader_dictionary(self):
        readerDictionary = {
            "imię czytelnika": self.name,
            "nazwisko czytelnika": self.surname,
            "numer czytelnika": self.number,
            "wypozyczone ksiazki": [],
            "oddane ksiazki": [],
        }
        return readerDictionary
