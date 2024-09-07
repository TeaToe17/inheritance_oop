class LibraryItem:

    def __init__(self, title: str, author: str, publication_year: str) -> None:
        self.__title: str = title
        self.__author: str = author
        self.__publication_year: str = publication_year

    def __str__(self) -> str:
        return f"Title: {self.__title}, Author: {self.__author}, Publication Year: {self.__publication_year}"


class Book(LibraryItem):
    
    def __init__(self, genre: str, isbn: str, *args) -> None:
        super().__init__(*args)
        self.__genre: str = genre
        self.__isbn: str = isbn
    
    def __str__(self) -> str:
        return (f"{super().__str__()}, "
                f"Genre: {self.__genre}, "
                f"ISBN: {self.__isbn}")


class Journal(LibraryItem):

    def __init__(self, volume: int, issue: int, *args) -> None:
        super().__init__(*args)
        self.__volume: int = volume
        self.__issue: int = issue
    
    def __str__(self) -> str:
        return (f"{super().__str__()}, "
                f"Volume: {self.__volume}, "
                f"Issue: {self.__issue}")


class Magazine(LibraryItem):

    def __init__(self, issue_month: str, editor: str, *args) -> None:
        super().__init__(*args)
        self.__issue_month: str = issue_month
        self.__editor: str = editor
    
    def __str__(self) -> str:
        return (f"{super().__str__()}, "
                f"Issue Month: {self.__issue_month}, "
                f"Editor: {self.__editor}")


class ReferenceBook(Book):

    def __init__(self, reference_section: str, *args) -> None:
        super().__init__(*args)
        self.__reference_section: str = reference_section

    def __str__(self) -> str:
        return (f"{super().__str__()}, "
                f"Reference Section: {self.__reference_section}")


# Example usage
book = Book("Fiction", "1234567890", "The Great Gatsby", "F. Scott Fitzgerald", "1925")
journal = Journal(10, 2, "Nature", "Various", "2022")
magazine = Magazine("July", "John Doe", "National Geographic", "Various", "2023")
ref_book = ReferenceBook("Section A", "General", "978-1234567890", "World Encyclopedia", "Various", "2020")

print(book)
print(journal)
print(magazine)
print(ref_book)
