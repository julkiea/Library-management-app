class Book:
    def __init__(
        self,
        title,
        writersName,
        writersSurname,
        literaryGenre,
        isbn,
        status="dostępna",
    ):
        self.writersName = writersName
        self.writersSurname = writersSurname
        self.title = title
        self.literaryGenre = literaryGenre
        self.status = status
        self.isbn = isbn

    def create_book_dictionary(self):
        bookDictionary = {
            "tytul": self.title,
            "imie autora": self.writersName,
            "nazwisko autora": self.writersSurname,
            "gatunek literacki": self.literaryGenre,
            "status": self.status,
            "isbn": self.isbn,
        }
        return bookDictionary
