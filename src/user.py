from datetime import date
from typing import Optional
from interfaces import Notifier


class User:
    def __init__(
        self,
        full_name: str,
        email: str = "",
        phone: str = "",
        address: str = "",
    ):
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.address = address


class Reader(User, Notifier):
    def __init__(
        self,
        full_name: str,
        email: str = "",
        phone: str = "",
        address: str = "",
        max_books: int = 3,
        notifier: Optional[Notifier] = None,
    ):
        super().__init__(full_name, email, phone, address)
        self.registration_date = date.today()
        self.status = "active"
        self.max_books = max_books
        self.notifier = notifier
        self._borrowed_books: list = []

    def update(self, message: str) -> None:
        print(f"{self.full_name}: {message}")

    def borrow_book(self, book) -> bool:
        if len(self._borrowed_books) >= self.max_books:
            return False
        if book in self._borrowed_books:
            return False
        if not book.borrow():
            return False
        self._borrowed_books.append(book)
        if self.notifier is not None:
            self.notifier.update(
                f"{self.full_name} взяла книгу: {book.title}"
            )
        return True

    def return_book(self, book) -> bool:
        if book not in self._borrowed_books:
            return False
        if not book.return_book():
            return False
        self._borrowed_books.remove(book)
        if self.notifier is not None:
            self.notifier.update(
                f"{self.full_name} повернула книгу: {book.title}"
            )
        return True


class Librarian(User):
    def __init__(
        self,
        full_name: str,
        employee_number: str,
        email: str = "",
        phone: str = "",
        address: str = "",
    ):
        super().__init__(full_name, email, phone, address)
        self.employee_number = employee_number

    def add_book_to_library(self, library, book) -> None:
        library.add_book(book)