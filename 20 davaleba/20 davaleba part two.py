class LibraryItem:
    def __init__(self, title, subject, status="available"):
        self.__title = title
        self.__subject = subject
        self.__status = status

    def booking(self):
        if self.__status == "occupied":
            print(f"The item '{self.__title}' is already booked.")
        else:
            self.__status = "occupied"
            print(f"You have successfully booked '{self.__title}'.")


class Book(LibraryItem):
    def __init__(self, title, subject, isbn, authors, status="available"):
        super().__init__(title, subject, status)
        self.__isbn = isbn
        self.__authors = authors


class Magazine(LibraryItem):
    def __init__(self, title, subject, journal_name, volume, status="available"):
        super().__init__(title, subject, status)
        self.journal_name = journal_name
        self.volume = volume


class CD(LibraryItem):
    def __init__(self, title, status="available"):
        super().__init__(title, "Music", status)

    def booking(self):
        print(f"CD '{self.status}' cannot be booked.")



book = Book("Python Programming", "Programming", "123456789", ["rakhmet kashmiri", "denis"])
magazine = Magazine("Science Weekly", "Science", "Nature Journal", 42)
cd = CD("Greatest Hits")

book.booking()
book.booking()
cd.booking()
