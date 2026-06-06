from typing import List
from interfaces import BookSearch


class Book:
    def __init__(
        self,
        title: str,
        author: str,
        publication_year: int,
        isbn: str,
        total_copies: int,
        genre: str = "Загальний",
    ):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn
        self.total_copies = total_copies
        self.genre = genre
        self._borrowed_count = 0

    @property
    def available_copies(self) -> int:
        return self.total_copies - self._borrowed_count

    @property
    def is_borrowed(self) -> bool:
        return self._borrowed_count >= self.total_copies

    def is_available(self) -> bool:
        return self.available_copies > 0

    def borrow(self) -> bool:
        if self.is_borrowed:
            return False
        self._borrowed_count += 1
        return True

    def return_book(self) -> bool:
        if self._borrowed_count == 0:
            return False
        self._borrowed_count -= 1
        return True

    def __str__(self) -> str:
        return f"{self.title} ({self.author}, {self.publication_year})"


class BookCopy:
    def __init__(self, inventory_number: str, status: str = "available"):
        self.inventory_number = inventory_number
        self.status = status

    def mark_as_borrowed(self) -> None:
        self.status = "borrowed"

    def mark_as_available(self) -> None:
        self.status = "available"


class Catalog(BookSearch):
    def __init__(self):
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, isbn: str) -> None:
        self._books = [book for book in self._books if book.isbn != isbn]

    def find_by_title(self, title: str) -> List[Book]:
        return [
            book
            for book in self._books
            if title.lower() in book.title.lower()
        ]

    def find_by_author(self, author: str) -> List[Book]:
        return [
            book
            for book in self._books
            if author.lower() in book.author.lower()
        ]

    def find_by_year(self, year: int) -> List[Book]:
        return [
            book
            for book in self._books
            if book.publication_year == year
        ]

    def get_all_books(self) -> List[Book]:
        return list(self._books)