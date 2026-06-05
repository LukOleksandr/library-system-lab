from datetime import date
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
    ):
        super().__init__(full_name, email, phone, address)
        self.registration_date = date.today()
        self.status = "active"

    def update(self, message: str) -> None:
        print(f"{self.full_name}: {message}")


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