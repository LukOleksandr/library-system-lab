from typing import List

from interfaces import Notifier, BookSearch
from book import Catalog, Book


class Library:
    _instance = None

    def __new__(
        cls,
        name: str = "Центральна бібліотека",
        address: str = "м. Київ",
    ):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(
        self,
        name: str = "Центральна бібліотека",
        address: str = "м. Київ",
    ):
        if self._initialized:
            return

        self.name = name
        self.address = address
        self.catalog = Catalog()
        self._observers: List[Notifier] = []
        self._initialized = True

    def attach(self, observer: Notifier) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Notifier) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)

    def add_book(self, book: Book) -> None:
        self.catalog.add_book(book)
        self.notify(f"Нова книга доступна - {book.title}")

    def get_book_search_service(self) -> BookSearch:
        return self.catalog

    def show_books(self) -> None:
        print("Список книг у бібліотеці:")
        for book in self.catalog.get_all_books():
            print(f"- {book}")
