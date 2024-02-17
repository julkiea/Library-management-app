import json
from book import Book
from reader import Reader


class Library:
    def __init__(self, nameOfLibrary, dataAboutBooks, dataAboutReaders):
        self.nameOfLibrary = nameOfLibrary
        self.dataAboutBooks = dataAboutBooks
        self.dataAboutReaders = dataAboutReaders

    def find_number_of_next_reader(self):
        with open(self.dataAboutReaders, "r") as json_file:
            python_data = json.load(json_file)
            listOfReaders = python_data["spisCzytelnikow"]
            number = int(listOfReaders[-1]["numer czytelnika"]) + 1
        return str(number)

    def add_a_book(self, newBook):
        bookToAdd = newBook.create_book_dictionary()
        try:
            with open(self.dataAboutBooks, "r") as json_file:
                python_data = json.load(json_file)
                listOfBooks = python_data["biblioteka"]
                listOfBooks.append(bookToAdd)
                python_data["biblioteka"] = listOfBooks
            with open(self.dataAboutBooks, "w") as json_file:
                json.dump(python_data, json_file, indent=2)
            text = "Książka została dodana pomyślnie"
            return text

        except FileNotFoundError:
            return "Plik nie istnieje"

    def delete_a_reader(self, name, surname, number):
        try:
            with open(self.dataAboutReaders, "r") as json_file:
                python_data = json.load(json_file)
                listOfReaders = python_data["spisCzytelnikow"]
                readerToBeDeleted = []
                for reader in listOfReaders:
                    if (
                        reader["imię czytelnika"] == name
                        and reader["nazwisko czytelnika"] == surname
                        and reader["numer czytelnika"] == number
                    ):
                        readerToBeDeleted.append(reader)
                if len(readerToBeDeleted) == 0:
                    text = "Podanego czytelnika nie ma w bibliotece"
                elif len(readerToBeDeleted) == 1:
                    rentalBooks = readerToBeDeleted[0]["wypozyczone ksiazki"]
                    if len(rentalBooks) >= 1:
                        text = "Podany czytelnik ma wypożyczone książki \n Nie możesz go usunąć"
                    else:
                        listOfReaders.remove(readerToBeDeleted[0])
                        python_data["spisCzytelnikow"] = listOfReaders
                        with open(self.dataAboutReaders, "w") as json_file:
                            json.dump(python_data, json_file, indent=2)
                        text = "Czytelnik został usunięcty pomyślnie"
            return text
        except FileNotFoundError:
            return "Nie znaleziono pliku"

    def delete_a_book(self, title, nameOfWriter, surnameOfWriter, isbn):
        try:
            with open(self.dataAboutBooks, "r") as json_file:
                python_data = json.load(json_file)
                listOfBooks = python_data["biblioteka"]
                booksToBeDeleted = []
                for book in listOfBooks:
                    if (
                        book["tytul"] == title
                        and book["imie autora"] == nameOfWriter
                        and book["nazwisko autora"] == surnameOfWriter
                        and book["isbn"] == isbn
                    ):
                        booksToBeDeleted.append(book)
                if len(booksToBeDeleted) == 0:
                    text = "Podanej książki nie ma w bibliotece"
                elif len(booksToBeDeleted) >= 1:
                    for book in booksToBeDeleted:
                        if book["status"] == "wypożyczona":
                            text = "Podana książka jest wypożyczona. \n Nie możesz jej usunąć"
                        else:
                            listOfBooks.remove(booksToBeDeleted[0])
                            python_data["biblioteka"] = listOfBooks
                            with open(self.dataAboutBooks, "w") as json_file:
                                json.dump(python_data, json_file, indent=2)
                            text = "Książka została usunięta pomyślnie"
            return text
        except FileNotFoundError:
            return "Plik nie istnieje"

    def return_a_book(
        self, nameOfReader, surnameOfReader, title, nameOfWriter, surnameOfWriter
    ):
        try:
            with open(self.dataAboutBooks, "r") as json_file:
                python_data = json.load(json_file)
                listOfBooks = python_data["biblioteka"]
                bookToBeAdded = []
                for book in listOfBooks:
                    if (
                        book["tytul"] == title
                        and book["imie autora"] == nameOfWriter
                        and book["nazwisko autora"] == surnameOfWriter
                        and book["status"] == "wypożyczona"
                    ):
                        bookToBeAdded.append(book)
                if len(bookToBeAdded) >= 1:
                    bookToBeAdded[0]["status"] = "dostępna"
                    python_data["biblioteka"] = listOfBooks
                    with open(self.dataAboutBooks, "w") as json_file:
                        json.dump(python_data, json_file, indent=2)

                    with open(self.dataAboutReaders, "r") as json_file:
                        python_data = json.load(json_file)
                        listOfReaders = python_data["spisCzytelnikow"]
                        readerWhoReturns = []

                        for reader in listOfReaders:
                            if (
                                reader["imię czytelnika"] == nameOfReader
                                and reader["nazwisko czytelnika"] == surnameOfReader
                            ):
                                readerWhoReturns.append(reader)
                        if len(readerWhoReturns) == 1:
                            text = "Książka została oddana pomyślnie"
                            listOfRentalBooks = readerWhoReturns[0][
                                "wypozyczone ksiazki"
                            ]
                            listOfReturnedBooks = readerWhoReturns[0]["oddane ksiazki"]
                            for ksiazka in listOfRentalBooks:
                                if (
                                    ksiazka["tytul"] == title
                                    and ksiazka["imie autora"] == nameOfWriter
                                    and ksiazka["nazwisko autora"] == surnameOfWriter
                                    and ksiazka["status"] == "wypożyczona"
                                ):
                                    listOfRentalBooks.remove(ksiazka)

                                    listOfReturnedBooks.append(ksiazka)
                            readerWhoReturns[0][
                                "wypozyczone ksiazki"
                            ] = listOfRentalBooks
                            readerWhoReturns[0]["oddane ksiazki"] = listOfReturnedBooks

                            with open(self.dataAboutReaders, "w") as json_file:
                                json.dump(python_data, json_file, indent=2)

                        else:
                            text = "Nie ma czytelnika o takim imieniu i nazwsisku"

                else:
                    text = "Nie udało się zwrócić książki"
                return text

        except FileNotFoundError:
            return "Plik nie istnieje"

    def borrow_a_book(
        self,
        nameOfReader,
        surnameOfReader,
        title,
        nameOfWriter,
        surnameOfWriter,
    ):
        try:
            with open(self.dataAboutBooks, "r") as json_file:
                python_data = json.load(json_file)
                listOfBooks = python_data["biblioteka"]
                booksToBeBorrowed = []
                for book in listOfBooks:
                    if (
                        book["tytul"] == title
                        and book["imie autora"] == nameOfWriter
                        and book["nazwisko autora"] == surnameOfWriter
                        and book["status"] == "dostępna"
                    ):
                        booksToBeBorrowed.append(book)

                if len(booksToBeBorrowed) >= 1:
                    booksToBeBorrowed[0]["status"] = "wypożyczona"
                    python_data["biblioteka"] = listOfBooks
                    with open(self.dataAboutBooks, "w") as json_file:
                        json.dump(python_data, json_file, indent=2)
                    with open(self.dataAboutReaders, "r") as json_file:
                        python_data = json.load(json_file)
                        listOfReaders = python_data["spisCzytelnikow"]
                        readerWhoBorrows = []

                        for reader in listOfReaders:
                            if (
                                reader["imię czytelnika"] == nameOfReader
                                and reader["nazwisko czytelnika"] == surnameOfReader
                            ):
                                readerWhoBorrows.append(reader)
                        if len(readerWhoBorrows) == 1:
                            text = "Książka została wypożyczona pomyślnie"
                            listOfRentalBooks = readerWhoBorrows[0][
                                "wypozyczone ksiazki"
                            ]
                            listOfRentalBooks.append(booksToBeBorrowed[0])
                            readerWhoBorrows[0][
                                "wypozyczone ksiazki"
                            ] = listOfRentalBooks
                            with open(self.dataAboutReaders, "w") as json_file:
                                json.dump(python_data, json_file, indent=2)

                        elif len(readerWhoBorrows) > 1:
                            text = "Jest więcej niż jeden czytelnik o takim imieniu i nazwisku"
                            booksToBeBorrowed[0]["status"] = "dostępna"
                            python_data["biblioteka"] = listOfBooks
                            with open(self.dataAboutBooks, "w") as json_file:
                                json.dump(python_data, json_file, indent=2)
                        else:
                            text = "Nie ma czytelnika o takim imieniu i nazwsisku"
                            booksToBeBorrowed[0]["status"] = "dostępna"
                            python_data["biblioteka"] = listOfBooks
                            with open(self.dataAboutBooks, "w") as json_file:
                                json.dump(python_data, json_file, indent=2)

                else:
                    text = "Podana książka nie jest dostępna"
                return text
        except FileNotFoundError:
            return "Plik nie istnieje"

    def add_a_reader(self, newReader):
        readerToBeAdded = newReader.create_reader_dictionary()
        try:
            with open(self.dataAboutReaders, "r") as json_file:
                python_data = json.load(json_file)
                listOfReaders = python_data["spisCzytelnikow"]
                listOfReaders.append(readerToBeAdded)
                python_data["spisCzytelnikow"] = listOfReaders
            with open(self.dataAboutReaders, "w") as json_file:
                json.dump(python_data, json_file, indent=2)
            text = "Czytelnik został dodany pomyślnie"
            return text
        except FileNotFoundError:
            return "Plik nie istnieje"

    def find_a_reader(self, name, surname):
        with open(self.dataAboutReaders, "r") as json_file:
            python_data = json.load(json_file)
            listOfReaders = python_data["spisCzytelnikow"]
            readerToBeFound = []
            for reader in listOfReaders:
                if (
                    reader["imię czytelnika"] == name
                    and reader["nazwisko czytelnika"] == surname
                ):
                    readerToBeFound.append(reader)
                else:
                    continue
            return readerToBeFound

    def find_a_book_with_title(self, title):
        with open(self.dataAboutBooks, "r") as json_file:
            python_data = json.load(json_file)
            listOfBooks = python_data["biblioteka"]
            booksWithTitle = []
            for book in listOfBooks:
                if book["tytul"] == title:
                    booksWithTitle.append(book)
                else:
                    continue
            return booksWithTitle

    def find_a_book_of_writer(self, name, surname):
        with open(self.dataAboutBooks, "r") as json_file:
            python_data = json.load(json_file)
            listOfBooks = python_data["biblioteka"]
            booksOfWriter = []
            for book in listOfBooks:
                if book["imie autora"] == name and book["nazwisko autora"] == surname:
                    booksOfWriter.append(book)
                else:
                    continue
            return booksOfWriter

    def find_a_book_with_writer_and_title(self, title, name, surname):
        with open(self.dataAboutBooks, "r") as json_file:
            python_data = json.load(json_file)
            listOfBooks = python_data["biblioteka"]
            booksOfWriterWithTitle = []
            for book in listOfBooks:
                if (
                    book["tytul"] == title
                    and book["imie autora"] == name
                    and book["nazwisko autora"] == surname
                ):
                    booksOfWriterWithTitle.append(book)
                else:
                    continue
            return booksOfWriterWithTitle

    def find_a_book_with_genre(self, genre):
        with open(self.dataAboutBooks, "r") as json_file:
            python_data = json.load(json_file)
            listOfBooks = python_data["biblioteka"]
            booksWithGenre = []
            for book in listOfBooks:
                if book["gatunek literacki"] == genre:
                    booksWithGenre.append(book)
                else:
                    continue
            return booksWithGenre

    def find_a_book_with_isbn(self, isbn):
        with open(self.dataAboutBooks, "r") as json_file:
            python_data = json.load(json_file)
            listOfBooks = python_data["biblioteka"]
            booksWithIsbn = []
            for book in listOfBooks:
                if book["isbn"] == isbn:
                    booksWithIsbn.append(book)
                else:
                    continue
            return booksWithIsbn

    def count_books_in_library(self):
        try:
            with open(self.dataAboutBooks, "r") as file:
                danePython = json.load(file)
                listOfBooks = len(danePython.get("biblioteka", []))
            return listOfBooks
        except FileNotFoundError:
            return "Nie znaleziono pliku o podanej nazwie."

    def count_readers_in_library(self):
        try:
            with open(self.dataAboutReaders, "r") as file:
                danePython = json.load(file)
                listOfReaders = len(danePython.get("spisCzytelnikow", []))
            return listOfReaders
        except FileNotFoundError:
            return "Nie znaleziono pliku o podanej nazwie."
