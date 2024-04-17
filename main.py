import customtkinter
from PIL import Image
from reader import Reader
from book import Book
from library import Library


library = Library("Moja Biblioteka", "library.json", "readers.json")


def add_a_book_button():
    addABookWindow = AddABookWindow()
    addABookWindow.mainloop()


def delete_a_reader_button():
    deleteAReaderWindow = DeleteAReaderWindow()
    deleteAReaderWindow.mainloop()


def delete_a_book_button():
    deleteABookWindow = DeleteABookWindow()
    deleteABookWindow.mainloop()


def return_a_book():
    returnABookWindow = ReturnABookWindow()
    returnABookWindow.mainloop()


def borrow_a_book_button():
    borrowABookWindow = BorrowABookWindow()
    borrowABookWindow.mainloop()


def add_a_reader_button():
    addAReaderWindow = AddAReaderWindow()
    addAReaderWindow.mainloop()


def find_a_reader_button():
    findAReaderWindow = FindAReaderWindow()
    findAReaderWindow.mainloop()


def find_a_book_button():
    findABookWindow = FindABookWindow()
    findABookWindow.mainloop()


def count_books_in_library_button():
    title = "Liczba książek"
    amountOfBooks = str(library.count_books_in_library())
    text = "Liczba książek \n w Twojej bibliotece wynosi: \n" + amountOfBooks

    windowWithMessage = SimpleWindow(title, text)
    windowWithMessage.mainloop()


def count_readers_in_library_button():
    title = "Liczba czytelników"
    amountOfReaders = str(library.count_readers_in_library())
    text = "Liczba czytelników \n w Twojej bibliotece wynosi: \n " + amountOfReaders

    windowWithMessage = SimpleWindow(title, text)
    windowWithMessage.mainloop()


class ReturnABookWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        self.title("Oddaj książkę")

        def confirm_returning_a_book_button():
            title = self.entry_title.get()
            nameOfWriter = self.entry_nameOfWriter.get()
            surnameOfWriter = self.entry_surnameOfWriter.get()
            nameOfReader = self.entry_nameOfReader.get()
            surnameOfReader = self.entry_surnameOfWriter.get()
            result = library.return_a_book(
                nameOfReader, surnameOfReader, title, nameOfWriter, surnameOfWriter
            )
            windowWithMessage = SimpleWindow("Informacja o oddaniu", result)
            windowWithMessage.mainloop()

        self.label_title = customtkinter.CTkLabel(
            self,
            text="Podaj tytuł książki: ",
            font=("Arial", 22),
            fg_color="#0F3624",
            text_color="white",
            width=400,
            height=40,
        )

        self.label_title.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.entry_title = customtkinter.CTkEntry(self, placeholder_text="Tytuł")
        self.entry_title.grid(row=0, column=1)
        self.entry_title.configure(state="normal")

        self.label_nameOfWriter = customtkinter.CTkLabel(
            self,
            text="Podaj imię autora książki: ",
            font=("Arial", 22),
            fg_color="#1A5539",
            text_color="white",
            width=400,
            height=40,
        )
        self.label_nameOfWriter.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.entry_nameOfWriter = customtkinter.CTkEntry(self, placeholder_text="Imię")
        self.entry_nameOfWriter.grid(row=1, column=1)
        self.entry_nameOfWriter.configure(state="normal")

        self.label_surnameOfWriter = customtkinter.CTkLabel(
            self,
            text="Podaj nazwisko autora książki: ",
            font=("Arial", 22),
            fg_color="#246F4C",
            text_color="white",
            width=400,
            height=40,
        )
        self.label_surnameOfWriter.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.entry_surnameOfWriter = customtkinter.CTkEntry(
            self, placeholder_text="Nazwisko"
        )
        self.entry_surnameOfWriter.grid(row=2, column=1)
        self.entry_surnameOfWriter.configure(state="normal")

        self.label = customtkinter.CTkLabel(
            self,
            text="Podaj imie czytelnika:",
            font=("Arial", 22),
            fg_color="#2D8A5F",
            text_color="white",
            width=400,
            height=40,
        )
        self.label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.entry_nameOfReader = customtkinter.CTkEntry(self, placeholder_text="Imię")
        self.entry_nameOfReader.grid(row=3, column=1)
        self.entry_nameOfReader.configure(state="normal")

        self.label = customtkinter.CTkLabel(
            self,
            text="Podaj nazwisko czytelnika:",
            font=("Arial", 22),
            fg_color="#3A9C6F",
            text_color="white",
            width=400,
            height=40,
        )
        self.label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        self.entry_surnameOfReader = customtkinter.CTkEntry(
            self, placeholder_text="Nazwisko"
        )
        self.entry_surnameOfReader.grid(row=4, column=1)
        self.entry_surnameOfReader.configure(state="normal")

        self.button_return = customtkinter.CTkButton(
            self,
            text="Oddaj książkę",
            font=("Arial", 22),
            fg_color="#4e0612",
            text_color="white",
            width=590,
            height=40,
            command=confirm_returning_a_book_button,
        )
        self.button_return.grid(row=5, column=0, padx=5, pady=5, columnspan=2)


class BorrowABookWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        self.title("Wypożycz książkę")

        def confirm_borrowing_a_book_button():
            title = self.entry_title.get()
            nameOfWriter = self.entry_nameOfWriter.get()
            surnameOfWriter = self.entry_surnameOfWriter.get()
            nameOfReader = self.entry_nameOfReader.get()
            surnameOfReader = self.entry_surnameOfReader.get()
            result = library.borrow_a_book(
                nameOfReader, surnameOfReader, title, nameOfWriter, surnameOfWriter
            )
            windowWithMessage = SimpleWindow("Informacja o wypożyczaniu", result)
            windowWithMessage.mainloop()

        self.label_title = customtkinter.CTkLabel(
            self,
            text="Podaj tytuł książki: ",
            font=("Arial", 22),
            fg_color="#0F3624",
            text_color="white",
            width=400,
            height=40,
        )

        self.label_title.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.entry_title = customtkinter.CTkEntry(self, placeholder_text="Tytuł")
        self.entry_title.grid(row=0, column=1)
        self.entry_title.configure(state="normal")

        self.label_nameOfWriter = customtkinter.CTkLabel(
            self,
            text="Podaj imię autora książki: ",
            font=("Arial", 22),
            fg_color="#1A5539",
            text_color="white",
            width=400,
            height=40,
        )
        self.label_nameOfWriter.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.entry_nameOfWriter = customtkinter.CTkEntry(self, placeholder_text="Imię")
        self.entry_nameOfWriter.grid(row=1, column=1)
        self.entry_nameOfWriter.configure(state="normal")

        self.label_surnameOfWriter = customtkinter.CTkLabel(
            self,
            text="Podaj nazwisko autora książki: ",
            font=("Arial", 22),
            fg_color="#246F4C",
            text_color="white",
            width=400,
            height=40,
        )
        self.label_surnameOfWriter.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.entry_surnameOfWriter = customtkinter.CTkEntry(
            self, placeholder_text="Nazwisko"
        )
        self.entry_surnameOfWriter.grid(row=2, column=1)
        self.entry_surnameOfWriter.configure(state="normal")

        self.label_nameOfReader = customtkinter.CTkLabel(
            self,
            text="Podaj imie czytelnika:",
            font=("Arial", 22),
            fg_color="#2D8A5F",
            text_color="white",
            width=400,
            height=40,
        )
        self.label_nameOfReader.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.entry_nameOfReader = customtkinter.CTkEntry(self, placeholder_text="Imię")
        self.entry_nameOfReader.grid(row=3, column=1)
        self.entry_nameOfReader.configure(state="normal")

        self.label_surnameOfReader = customtkinter.CTkLabel(
            self,
            text="Podaj nazwisko czytelnika:",
            font=("Arial", 22),
            fg_color="#3A9C6F",
            text_color="white",
            width=400,
            height=40,
        )
        self.label_surnameOfReader.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        self.entry_surnameOfReader = customtkinter.CTkEntry(
            self, placeholder_text="Nazwisko"
        )
        self.entry_surnameOfReader.grid(row=4, column=1)
        self.entry_surnameOfReader.configure(state="normal")

        self.button_borrow = customtkinter.CTkButton(
            self,
            text="Wypożycz książkę",
            font=("Arial", 22),
            fg_color="#4e0612",
            text_color="white",
            width=590,
            height=40,
            command=confirm_borrowing_a_book_button,
        )
        self.button_borrow.grid(row=5, column=0, padx=5, pady=5, columnspan=2)


class FindABookWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x650")
        self.title("Wyszukaj książkę")

        def confirm_looking_for_book_with_title_button():
            title = self.entry_title.get()
            result = library.find_a_book_with_title(title)
            books = []
            if len(result) == 0:
                windowWithMessage = SimpleWindow(
                    "Nie znaleziono książki",
                    "Nie znaleziono książki \n o podanym tytule",
                )
                windowWithMessage.mainloop()
            else:
                for book in result:
                    text = (
                        "Znaleziono książkę: \n Tytuł: "
                        + book["tytul"]
                        + "\n Autor: "
                        + book["imie autora"]
                        + " "
                        + book["nazwisko autora"]
                        + "\n Status: "
                        + book["status"]
                        + "\n Gatunek literacki: "
                        + book["gatunek literacki"]
                        + "\n Isbn: "
                        + book["isbn"]
                    )
                    books.append(text)
                windowWithScrollableLabels = WindowWithScrollableLabels(
                    "Znalezione książki", books
                )
                windowWithScrollableLabels.mainloop()

        def confirm_looking_for_book_with_genre_button():
            genre = self.entry_genre.get()
            result = library.find_a_book_with_genre(genre)
            books = []
            if len(result) == 0:
                windowWithMessage = SimpleWindow(
                    "Nie znaleziono książki",
                    "Nie znaleziono książki \n o podanym gatunku literackim",
                )
                windowWithMessage.mainloop()
            else:
                for book in result:
                    text = (
                        "Znaleziono książkę: \n Tytuł: "
                        + book["tytul"]
                        + "\n Autor: "
                        + book["imie autora"]
                        + " "
                        + book["nazwisko autora"]
                        + "\n Status: "
                        + book["status"]
                        + "\n Gatunek literacki: "
                        + book["gatunek literacki"]
                        + "\n Isbn: "
                        + book["isbn"]
                    )
                    books.append(text)
                windowWithScrollableLabels = WindowWithScrollableLabels(
                    "Znalezione książki", books
                )
                windowWithScrollableLabels.mainloop()

        def confirm_looking_for_book_with_isbn_button():
            isbn = self.entry_isbn.get()
            result = library.find_a_book_with_isbn(isbn)
            books = []
            if len(result) == 0:
                windowWithMessage = SimpleWindow(
                    "Nie znaleziono książki",
                    "Nie znaleziono książki \n o podanym isbn",
                )
                windowWithMessage.mainloop()
            else:
                for book in result:
                    text = (
                        "Znaleziono książkę: \n Tytuł: "
                        + book["tytul"]
                        + "\n Autor: "
                        + book["imie autora"]
                        + " "
                        + book["nazwisko autora"]
                        + "\n Status: "
                        + book["status"]
                        + "\n Gatunek literacki: "
                        + book["gatunek literacki"]
                        + "\n Isbn: "
                        + book["isbn"]
                    )
                    books.append(text)
                windowWithScrollableLabels = WindowWithScrollableLabels(
                    "Znalezione książki", books
                )
                windowWithScrollableLabels.mainloop()

        def confirm_looking_for_book_with_writer_button():
            name = self.entry_nameOfWriter.get()
            surname = self.entry_surnameOfWriter.get()
            result = library.find_a_book_of_writer(name, surname)
            books = []
            if len(result) == 0:
                windowWithMessage = SimpleWindow(
                    "Nie znaleziono książki",
                    "Nie znaleziono książki \n podanego autora",
                )
                windowWithMessage.mainloop()
            else:
                for book in result:
                    text = (
                        "Znaleziono książkę: \n Tytuł: "
                        + book["tytul"]
                        + "\n Autor: "
                        + book["imie autora"]
                        + " "
                        + book["nazwisko autora"]
                        + "\n Status: "
                        + book["status"]
                        + "\n Gatunek literacki: "
                        + book["gatunek literacki"]
                        + "\n Isbn: "
                        + book["isbn"]
                    )
                    books.append(text)
                windowWithScrollableLabels = WindowWithScrollableLabels(
                    "Znalezione książki", books
                )
                windowWithScrollableLabels.mainloop()

        def confirm_looking_for_book_with_writer_and_title_button():
            title = self.entry_title2.get()
            name = self.entry_nameOfWriter2.get()
            surname = self.entry_surnameOfWriter2.get()
            result = library.find_a_book_with_writer_and_title(title, name, surname)
            books = []
            if len(result) == 0:
                windowWithMessage = SimpleWindow(
                    "Nie znaleziono książki",
                    "Nie znaleziono książki \n o podanym tytule \n podanego autora",
                )
                windowWithMessage.mainloop()
            else:
                for book in result:
                    text = (
                        "Znaleziono książkę: \n Tytuł: "
                        + book["tytul"]
                        + "\n Autor: "
                        + book["imie autora"]
                        + " "
                        + book["nazwisko autora"]
                        + "\n Status: "
                        + book["status"]
                        + "\n Gatunek literacki: "
                        + book["gatunek literacki"]
                        + "\n Isbn: "
                        + book["isbn"]
                    )
                    books.append(text)
                windowWithScrollableLabels = WindowWithScrollableLabels(
                    "Znalezione książki", books
                )
                windowWithScrollableLabels.mainloop()

        self.label_title = customtkinter.CTkLabel(
            self,
            text="Podaj tytuł książki: ",
            font=("Arial", 22),
            fg_color="#10492e",
            text_color="white",
            width=400,
            height=40,
        )
        self.label_title.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.entry_title = customtkinter.CTkEntry(self, placeholder_text="Tytuł")
        self.entry_title.grid(row=0, column=1)
        self.entry_title.configure(state="normal")

        self.button_withtitle = customtkinter.CTkButton(
            self,
            text="Wyszukaj po tytule",
            font=("Arial", 22),
            fg_color="#4e0612",
            text_color="white",
            width=590,
            height=40,
            command=confirm_looking_for_book_with_title_button,
        )
        self.button_withtitle.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        self.label_nameOfWriter = customtkinter.CTkLabel(
            self,
            text="Podaj imię autora książki: ",
            font=("Arial", 22),
            fg_color="#155839",
            text_color="white",
            width=400,
            height=40,
        )
        self.label_nameOfWriter.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.entry_nameOfWriter = customtkinter.CTkEntry(self, placeholder_text="Imię")
        self.entry_nameOfWriter.grid(row=2, column=1)
        self.entry_nameOfWriter.configure(state="normal")

        self.label_surnameOfWriter = customtkinter.CTkLabel(
            self,
            text="Podaj nazwisko autora książki: ",
            font=("Arial", 22),
            fg_color="#155839",
            text_color="white",
            width=400,
            height=40,
        )
        self.label_surnameOfWriter.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.entry_surnameOfWriter = customtkinter.CTkEntry(
            self, placeholder_text="Nazwisko"
        )
        self.entry_surnameOfWriter.grid(row=3, column=1)
        self.entry_surnameOfWriter.configure(state="normal")

        self.button_withWriter = customtkinter.CTkButton(
            self,
            text="Wyszukaj po autorze",
            font=("Arial", 22),
            fg_color="#4e0612",
            text_color="white",
            width=590,
            height=40,
            command=confirm_looking_for_book_with_writer_button,
        )
        self.button_withWriter.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

        self.label_title2 = customtkinter.CTkLabel(
            self,
            text="Podaj tytuł książki: ",
            font=("Arial", 22),
            fg_color="#1b6f48",
            text_color="white",
            width=400,
            height=40,
        )
        self.label_title2.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        self.entry_title2 = customtkinter.CTkEntry(self, placeholder_text="Tytuł")
        self.entry_title2.grid(row=5, column=1)
        self.entry_title2.configure(state="normal")

        self.label_nameOfWriter2 = customtkinter.CTkLabel(
            self,
            text="Podaj imię autora książki: ",
            font=("Arial", 22),
            fg_color="#228657",
            text_color="white",
            width=400,
            height=40,
        )
        self.label_nameOfWriter2.grid(row=6, column=0, padx=5, pady=5, sticky="w")

        self.entry_nameOfWriter2 = customtkinter.CTkEntry(self, placeholder_text="Imię")
        self.entry_nameOfWriter2.grid(row=6, column=1)
        self.entry_nameOfWriter2.configure(state="normal")

        self.label_surnameOfWriter2 = customtkinter.CTkLabel(
            self,
            text="Podaj nazwisko autora książki: ",
            font=("Arial", 22),
            fg_color="#228657",
            text_color="white",
            width=400,
            height=40,
        )
        self.label_surnameOfWriter2.grid(row=7, column=0, padx=5, pady=5, sticky="w")

        self.entry_surnameOfWriter2 = customtkinter.CTkEntry(
            self, placeholder_text="Nazwisko"
        )
        self.entry_surnameOfWriter2.grid(row=7, column=1)
        self.entry_surnameOfWriter2.configure(state="normal")

        self.button_withWriterAndTitle = customtkinter.CTkButton(
            self,
            text="Wyszukaj po tytule i autorze",
            font=("Arial", 22),
            fg_color="#4e0612",
            text_color="white",
            width=590,
            height=40,
            command=confirm_looking_for_book_with_writer_and_title_button,
        )
        self.button_withWriterAndTitle.grid(
            row=8, column=0, padx=5, pady=5, columnspan=2
        )

        self.label_genre = customtkinter.CTkLabel(
            self,
            text="Podaj gatunek literacki książki: ",
            font=("Arial", 22),
            fg_color="#279763",
            text_color="white",
            width=400,
            height=40,
        )
        self.label_genre.grid(row=9, column=0, padx=5, pady=5, sticky="w")

        self.entry_genre = customtkinter.CTkEntry(
            self, placeholder_text="Gatunek literacki"
        )
        self.entry_genre.grid(row=9, column=1)
        self.entry_genre.configure(state="normal")

        self.button_withGenre = customtkinter.CTkButton(
            self,
            text="Wyszukaj po gatunku literackim",
            font=("Arial", 22),
            fg_color="#4e0612",
            text_color="white",
            width=590,
            height=40,
            command=confirm_looking_for_book_with_genre_button,
        )
        self.button_withGenre.grid(row=10, column=0, padx=5, pady=5, columnspan=2)

        self.label_isbn = customtkinter.CTkLabel(
            self,
            text="Podaj gatunek literacki książki: ",
            font=("Arial", 22),
            fg_color="#47ab7c",
            text_color="white",
            width=400,
            height=40,
        )
        self.label_isbn.grid(row=11, column=0, padx=5, pady=5, sticky="w")

        self.entry_isbn = customtkinter.CTkEntry(self, placeholder_text="Isbn")
        self.entry_isbn.grid(row=11, column=1)
        self.entry_isbn.configure(state="normal")

        self.button_withIsbn = customtkinter.CTkButton(
            self,
            text="Wyszukaj po isbn:",
            font=("Arial", 22),
            fg_color="#4e0612",
            text_color="white",
            width=590,
            height=40,
            command=confirm_looking_for_book_with_isbn_button,
        )
        self.button_withIsbn.grid(row=12, column=0, padx=5, pady=5, columnspan=2)


class FrameWithLabels(customtkinter.CTkScrollableFrame):
    def __init__(self, master, values, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.labels = []

        for i, value in enumerate(self.values):
            label = customtkinter.CTkLabel(
                self,
                text=value,
                font=("Arial", 14),
                fg_color="#1D6845",
                text_color="white",
                width=350,
                height=50,
            )
            label.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.labels.append(label)


class WindowWithScrollableLabels(customtkinter.CTk):
    def __init__(self, title, labels):
        super().__init__()
        self.geometry("400x300")
        self.title(title)
        self.labels = labels
        self.scrollable_frame = FrameWithLabels(
            self, values=self.labels, width=360, height=260
        )

        self.scrollable_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")


class FindAReaderWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x200")
        self.title("Wyszukaj czytelnika")
        self.results = []

        def confirm_looking_for_reader():
            nameOfReader = self.entry_nameOfReader.get()
            surnameOfReader = self.entry_surnameOfReader.get()
            result = library.find_a_reader(nameOfReader, surnameOfReader)
            readers = []
            if len(result) == 0:
                windowWithMessage = SimpleWindow(
                    "Nie znaleziono czytelnika", "Nie znaleziono czytelnika"
                )
                windowWithMessage.mainloop()
            else:
                for czytelnik in result:
                    wypozyczoneKsiazki = czytelnik["wypozyczone ksiazki"]
                    oddaneKsiazki = czytelnik["oddane ksiazki"]

                    tekst_czytelnik = (
                        "Znaleziono czytelnika: \n Imię: "
                        + czytelnik["imię czytelnika"]
                        + "\n Nazwisko: "
                        + czytelnik["nazwisko czytelnika"]
                        + "\n Numer: "
                        + czytelnik["numer czytelnika"]
                    )
                    if wypozyczoneKsiazki:
                        for ksiazka in wypozyczoneKsiazki:
                            tekst_czytelnik += (
                                "\nWypożyczone książki: "
                                "\n - Tytuł: "
                                + ksiazka["tytul"]
                                + ", \nAutor: "
                                + ksiazka["imie autora"]
                                + " "
                                + ksiazka["nazwisko autora"]
                            )
                    if oddaneKsiazki:
                        for ksiazka in oddaneKsiazki:
                            tekst_czytelnik += (
                                "\nOddane książki: "
                                "\n - Tytuł: "
                                + ksiazka["tytul"]
                                + ", \nAutor: "
                                + ksiazka["imie autora"]
                                + " "
                                + ksiazka["nazwisko autora"]
                            )
                    readers.append(tekst_czytelnik)
                windowWithScrollableLabels = WindowWithScrollableLabels(
                    "Znalezieni czytelnicy", readers
                )
                windowWithScrollableLabels.mainloop()

        self.label = customtkinter.CTkLabel(
            self,
            text="Podaj imie czytelnika:",
            font=("Arial", 22),
            fg_color="#10492e",
            text_color="white",
            width=400,
            height=50,
        )
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.entry_nameOfReader = customtkinter.CTkEntry(self, placeholder_text="Imię")
        self.entry_nameOfReader.grid(row=0, column=1)
        self.entry_nameOfReader.configure(state="normal")

        self.label = customtkinter.CTkLabel(
            self,
            text="Podaj nazwisko czytelnika:",
            font=("Arial", 22),
            fg_color="#155b3a",
            text_color="white",
            width=400,
            height=50,
        )
        self.label.grid(row=1, column=0, padx=5, pady=5)

        self.entry_surnameOfReader = customtkinter.CTkEntry(
            self, placeholder_text="Nazwisko"
        )
        self.entry_surnameOfReader.grid(row=1, column=1)
        self.entry_surnameOfReader.configure(state="normal")

        self.button = customtkinter.CTkButton(
            self,
            text="Wyświetl kartę czytelnika",
            fg_color="#4e0612",
            font=("Arial", 22),
            text_color="white",
            width=590,
            height=50,
            command=confirm_looking_for_reader,
        )
        self.button.grid(row=5, column=0, padx=5, pady=5, columnspan=2)


class AddAReaderWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x250")
        self.title("Dodaj czytelnika")
        self.results = []

        def confirm_adding_a_reader_button():
            nameOfReader = self.entry_nameOfReader.get()
            surnameOfReader = self.entry_surnameOfReader.get()
            numberOfReader = self.entry_numberOfReader.get()

            newReader = Reader(nameOfReader, surnameOfReader, numberOfReader)
            result = library.add_a_reader(newReader)
            windowWithMessage = SimpleWindow("Dodano czytelnika", result)
            windowWithMessage.mainloop()

        self.label = customtkinter.CTkLabel(
            self,
            text="Podaj imie czytelnika:",
            font=("Arial", 22),
            fg_color="#0F3624",
            text_color="white",
            width=400,
            height=50,
        )
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.entry_nameOfReader = customtkinter.CTkEntry(self, placeholder_text="Imię")
        self.entry_nameOfReader.grid(row=0, column=1)
        self.entry_nameOfReader.configure(state="normal")

        self.label = customtkinter.CTkLabel(
            self,
            text="Podaj nazwisko czytelnika:",
            font=("Arial", 22),
            fg_color="#12472E",
            text_color="white",
            width=400,
            height=50,
        )
        self.label.grid(row=1, column=0, padx=5, pady=5)

        self.entry_surnameOfReader = customtkinter.CTkEntry(
            self, placeholder_text="Nazwisko"
        )
        self.entry_surnameOfReader.grid(row=1, column=1)
        self.entry_surnameOfReader.configure(state="normal")

        self.label = customtkinter.CTkLabel(
            self,
            text=(
                "Nadaj numer czytelnikowi: \n (sugerowany numer: "
                + str(library.find_number_of_next_reader())
                + ")"
            ),
            font=("Arial", 21),
            fg_color="#1B6542",
            text_color="white",
            width=400,
            height=50,
        )
        self.label.grid(row=2, column=0, padx=5, pady=5)

        self.entry_numberOfReader = customtkinter.CTkEntry(
            self, placeholder_text="Numer"
        )
        self.entry_numberOfReader.grid(row=2, column=1)
        self.entry_numberOfReader.configure(state="normal")

        self.button = customtkinter.CTkButton(
            self,
            text="Zatwierdź",
            fg_color="#4e0612",
            font=("Arial", 22),
            text_color="white",
            width=590,
            height=50,
            command=confirm_adding_a_reader_button,
        )
        self.button.grid(row=5, column=0, padx=5, pady=5, columnspan=2)


class DeleteAReaderWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x250")
        self.title("Usuń czytelnika")
        self.results = []

        def confirm_deleting_reader_button():
            nameOfReader = self.entry_name.get()
            surnameOfReader = self.entry_surname.get()
            numberOfReader = self.entry_number.get()

            result = library.delete_a_reader(
                nameOfReader, surnameOfReader, numberOfReader
            )
            windowWithMessage = SimpleWindow(
                "Informacja o usunięciu czytelnika", result
            )
            windowWithMessage.mainloop()

        self.label = customtkinter.CTkLabel(
            self,
            text="Podaj imie czytelnika:",
            font=("Arial", 22),
            fg_color="#0F3624",
            text_color="white",
            width=400,
            height=50,
        )
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.entry_name = customtkinter.CTkEntry(self, placeholder_text="Imię")
        self.entry_name.grid(row=0, column=1)
        self.entry_name.configure(state="normal")

        self.label = customtkinter.CTkLabel(
            self,
            text="Podaj nazwisko czytelnika:",
            font=("Arial", 22),
            fg_color="#12472E",
            text_color="white",
            width=400,
            height=50,
        )
        self.label.grid(row=1, column=0, padx=5, pady=5)

        self.entry_surname = customtkinter.CTkEntry(self, placeholder_text="Nazwisko")
        self.entry_surname.grid(row=1, column=1)
        self.entry_surname.configure(state="normal")

        self.label = customtkinter.CTkLabel(
            self,
            text=("Podaj numer czytelnika:"),
            font=("Arial", 21),
            fg_color="#1B6542",
            text_color="white",
            width=400,
            height=50,
        )
        self.label.grid(row=2, column=0, padx=5, pady=5)

        self.entry_number = customtkinter.CTkEntry(self, placeholder_text="Numer")
        self.entry_number.grid(row=2, column=1)
        self.entry_number.configure(state="normal")

        self.button = customtkinter.CTkButton(
            self,
            text="Zatwierdź",
            fg_color="#4e0612",
            font=("Arial", 22),
            text_color="white",
            width=590,
            height=50,
            command=confirm_deleting_reader_button,
        )
        self.button.grid(row=5, column=0, padx=5, pady=5, columnspan=2)


class DeleteABookWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        self.title("Usuń książkę")
        self.results = []

        def confirm_deleting_book_button():
            title = self.entry_title.get()
            name = self.entry_name.get()
            surname = self.entry_surname.get()
            isbn = self.entry_isbn.get()

            result = library.delete_a_book(title, name, surname, isbn)
            windowWithMessage = SimpleWindow("Informacja o usuwaniu książki", result)
            windowWithMessage.mainloop()

        self.label = customtkinter.CTkLabel(
            self,
            text="Podaj tytuł książki:",
            font=("Arial", 22),
            fg_color="#0F3624",
            text_color="white",
            width=400,
            height=50,
        )
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.entry_title = customtkinter.CTkEntry(self, placeholder_text="Tytuł")
        self.entry_title.grid(row=0, column=1)
        self.entry_title.configure(state="normal")

        self.label = customtkinter.CTkLabel(
            self,
            text="Podaj imię autora książki:",
            font=("Arial", 22),
            fg_color="#12472E",
            text_color="white",
            width=400,
            height=50,
        )
        self.label.grid(row=1, column=0, padx=5, pady=5)

        self.entry_name = customtkinter.CTkEntry(self, placeholder_text="Imię")
        self.entry_name.grid(row=1, column=1)
        self.entry_name.configure(state="normal")

        self.label = customtkinter.CTkLabel(
            self,
            text="Podaj nazwisko autora książki:",
            font=("Arial", 22),
            fg_color="#1B6542",
            text_color="white",
            width=400,
            height=50,
        )
        self.label.grid(row=2, column=0, padx=5, pady=5)

        self.entry_surname = customtkinter.CTkEntry(self, placeholder_text="Nazwisko")
        self.entry_surname.grid(row=2, column=1)
        self.entry_surname.configure(state="normal")

        self.label = customtkinter.CTkLabel(
            self,
            text="Podaj isbn:",
            font=("Arial", 22),
            fg_color="#309767",
            text_color="white",
            width=400,
            height=50,
        )
        self.label.grid(row=3, column=0, padx=5, pady=5)

        self.entry_isbn = customtkinter.CTkEntry(self, placeholder_text="isbn")
        self.entry_isbn.grid(row=3, column=1)
        self.entry_isbn.configure(state="normal")

        self.button = customtkinter.CTkButton(
            self,
            text="Zatwierdź",
            fg_color="#4e0612",
            font=("Arial", 22),
            text_color="white",
            width=590,
            height=50,
            command=confirm_deleting_book_button,
        )
        self.button.grid(row=4, column=0, padx=5, pady=5, columnspan=2)


class AddABookWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x360")
        self.title("Dodaj książkę")
        self.results = []

        def confirm_adding_book_button():
            title = self.entry_title.get()
            name = self.entry_name.get()
            surname = self.entry_surname.get()
            genre = self.entry_genre.get()
            isbn = self.entry_isbn.get()
            self.results = [title, name, surname, genre, isbn]
            title = self.results[0]

            nameOfWriter = self.results[1]

            surnameOfWriter = self.results[2]

            literaryGenre = self.results[3]

            isbn = self.results[4]

            newBook = Book(title, nameOfWriter, surnameOfWriter, literaryGenre, isbn)
            result = library.add_a_book(newBook)
            windowWithMessage = SimpleWindow("Dodano książkę", result)
            windowWithMessage.mainloop()
            # AddABookWindow.destroy()

        self.label = customtkinter.CTkLabel(
            self,
            text="Podaj tytuł książki:",
            font=("Arial", 22),
            fg_color="#0F3624",
            text_color="white",
            width=400,
            height=50,
        )
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.entry_title = customtkinter.CTkEntry(self, placeholder_text="Tytuł")
        self.entry_title.grid(row=0, column=1)
        self.entry_title.configure(state="normal")

        self.label = customtkinter.CTkLabel(
            self,
            text="Podaj imię autora książki:",
            font=("Arial", 22),
            fg_color="#12472E",
            text_color="white",
            width=400,
            height=50,
        )
        self.label.grid(row=1, column=0, padx=5, pady=5)

        self.entry_name = customtkinter.CTkEntry(self, placeholder_text="Imię")
        self.entry_name.grid(row=1, column=1)
        self.entry_name.configure(state="normal")

        self.label = customtkinter.CTkLabel(
            self,
            text="Podaj nazwisko autora książki:",
            font=("Arial", 22),
            fg_color="#1B6542",
            text_color="white",
            width=400,
            height=50,
        )
        self.label.grid(row=2, column=0, padx=5, pady=5)

        self.entry_surname = customtkinter.CTkEntry(self, placeholder_text="Nazwisko")
        self.entry_surname.grid(row=2, column=1)
        self.entry_surname.configure(state="normal")

        self.label = customtkinter.CTkLabel(
            self,
            text="Podaj gatunek literacki:",
            font=("Arial", 22),
            fg_color="#247C53",
            text_color="white",
            width=400,
            height=50,
        )
        self.label.grid(row=3, column=0, padx=5, pady=5)

        self.entry_genre = customtkinter.CTkEntry(
            self, placeholder_text="Gatunek literacki"
        )
        self.entry_genre.grid(row=3, column=1)
        self.entry_genre.configure(state="normal")

        self.label = customtkinter.CTkLabel(
            self,
            text="Podaj isbn:",
            font=("Arial", 22),
            fg_color="#309767",
            text_color="white",
            width=400,
            height=50,
        )
        self.label.grid(row=4, column=0, padx=5, pady=5)

        self.entry_isbn = customtkinter.CTkEntry(self, placeholder_text="isbn")
        self.entry_isbn.grid(row=4, column=1)
        self.entry_isbn.configure(state="normal")

        self.button = customtkinter.CTkButton(
            self,
            text="Zatwierdź",
            fg_color="#4e0612",
            font=("Arial", 22),
            text_color="white",
            width=590,
            height=50,
            command=confirm_adding_book_button,
        )
        self.button.grid(row=5, column=0, padx=5, pady=5, columnspan=2)


class BooksFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.button = customtkinter.CTkButton(
            self,
            text="Dodaj książkę",
            font=("Arial", 18),
            fg_color="#10492e",
            text_color="white",
            width=370,
            height=50,
            command=add_a_book_button,
        )
        self.button.grid(row=0, column=0, padx=5, pady=5)

        self.button = customtkinter.CTkButton(
            self,
            text="Wyszukaj książkę",
            font=("Arial", 18),
            fg_color="#176541",
            text_color="white",
            width=370,
            height=50,
            command=find_a_book_button,
        )
        self.button.grid(row=1, column=0, padx=5, pady=5)

        self.button = customtkinter.CTkButton(
            self,
            text="Usuń książkę",
            font=("Arial", 18),
            fg_color="#208757",
            text_color="white",
            width=370,
            height=50,
            command=delete_a_book_button,
        )
        self.button.grid(row=2, column=0, padx=5, pady=5)

        self.button = customtkinter.CTkButton(
            self,
            text="Wypożycz książkę",
            font=("Arial", 18),
            fg_color="#2cb073",
            text_color="white",
            width=370,
            height=50,
            command=borrow_a_book_button,
        )
        self.button.grid(row=3, column=0, padx=5, pady=5)


class SimpleWindow(customtkinter.CTk):
    def __init__(self, tytul, tekst):
        super().__init__()
        self.geometry("400x300")
        self.title(tytul)
        self.text = tekst

        self.label = customtkinter.CTkLabel(
            self,
            text=self.text,
            width=390,
            height=290,
            fg_color="#176541",
            font=("Arial", 20),
            text_color="white",
        )
        self.label.grid(row=0, column=0, padx=5, pady=5)


class LibraryFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.button = customtkinter.CTkButton(
            self,
            text="Sprawdź liczbę książek",
            font=("Arial", 18),
            fg_color="#10492e",
            text_color="white",
            width=370,
            height=50,
            command=count_books_in_library_button,
        )
        self.button.grid(row=0, column=0, padx=5, pady=5)

        self.button = customtkinter.CTkButton(
            self,
            text="Sprawdź liczbę czytelników",
            font=("Arial", 18),
            fg_color="#10492e",
            text_color="white",
            width=390,
            height=50,
            command=count_readers_in_library_button,
        )
        self.button.grid(row=0, column=1, padx=5, pady=5)


class ReadersFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.button = customtkinter.CTkButton(
            self,
            text="Dodaj czytelnika",
            font=("Arial", 18),
            fg_color="#10492e",
            text_color="white",
            width=390,
            height=50,
            command=add_a_reader_button,
        )
        self.button.grid(row=0, column=0, padx=5, pady=5)

        self.button = customtkinter.CTkButton(
            self,
            text="Wyświetl kartę czytelnika",
            font=("Arial", 18),
            fg_color="#176541",
            text_color="white",
            width=390,
            height=50,
            command=find_a_reader_button,
        )
        self.button.grid(row=1, column=0, padx=5, pady=5)

        self.button = customtkinter.CTkButton(
            self,
            text="Usuń czytelnika",
            font=("Arial", 18),
            fg_color="#208757",
            text_color="white",
            width=390,
            height=50,
            command=delete_a_reader_button,
        )
        self.button.grid(row=2, column=0, padx=5, pady=5)

        self.button = customtkinter.CTkButton(
            self,
            text="Oddaj książkę",
            font=("Arial", 18),
            fg_color="#2cb073",
            text_color="white",
            width=390,
            height=50,
            command=return_a_book,
        )
        self.button.grid(row=3, column=0, padx=5, pady=5)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Biblioteka")
        self.geometry("800x700")
        self.grid_columnconfigure((0, 5), weight=1)

        self.label = customtkinter.CTkLabel(
            self,
            text="Witaj! \n Oto Twoja aplikacja \n do zarządzania biblioteką. \n Mamy nadzieję, \n że znajdziesz tu wszystko, \n czego potrzebujesz.",
            font=("Arial Black", 21),
            fg_color="#125a42",
            text_color="white",
            width=400,
            height=250,
        )
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        my_image = customtkinter.CTkImage(
            light_image=Image.open(".\libraryphoto.jpg"), size=(400, 250)
        )
        self.label = customtkinter.CTkLabel(
            self, image=my_image, text="", width=400, height=250
        )
        self.label.grid(row=0, column=1, padx=5, pady=5, sticky="e")

        self.label = customtkinter.CTkLabel(
            self,
            text="Książka",
            font=("Arial Black", 18),
            fg_color="#093224",
            text_color="white",
            width=400,
            height=40,
        )
        self.label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.label = customtkinter.CTkLabel(
            self,
            text="Czytelnik",
            font=("Arial Black", 18),
            fg_color="#093224",
            text_color="white",
            width=400,
            height=40,
        )
        self.label.grid(row=1, column=1, padx=5, pady=5, sticky="e")

        self.booksFrame = BooksFrame(master=self, width=410)
        self.booksFrame.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        self.readersFrame = ReadersFrame(master=self, width=400)
        self.readersFrame.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        self.label = customtkinter.CTkLabel(
            self,
            text="Biblioteka",
            font=("Arial Black", 18),
            fg_color="#093224",
            text_color="white",
            width=800,
            height=50,
        )
        self.label.grid(row=3, column=0, padx=5, pady=5, sticky="ew", columnspan=2)

        self.libraryFrame = LibraryFrame(master=self, width=800)
        self.libraryFrame.grid(row=4, column=0, padx=5, pady=5, columnspan=2)


app = App()
app.mainloop()
