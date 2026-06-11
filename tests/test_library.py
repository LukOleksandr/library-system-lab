import os
import sys
import unittest
from unittest.mock import Mock

SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.insert(0, SRC_DIR)

from book import Book
from interfaces import Notifier
from library import Library


class TestLibrary(unittest.TestCase):

    def tearDown(self):
        Library._instance = None
        if hasattr(Library, "_observers"):
            Library._observers = []

    def test_singleton_returns_same_instance(self):
        lib1 = Library("Перша бібліотека", "вул. Шевченка, 1")
        lib2 = Library("Друга бібліотека", "вул. Франка, 2")

        self.assertIs(lib1, lib2)

    def test_attach_adds_observer(self):
        library = Library()
        mock_observer = Mock(spec=Notifier)

        library.attach(mock_observer)

        self.assertIn(mock_observer, library._observers)

    def test_attach_does_not_duplicate_observer(self):
        library = Library()
        mock_observer = Mock(spec=Notifier)

        library.attach(mock_observer)
        library.attach(mock_observer)

        self.assertEqual(library._observers.count(mock_observer), 1)

    def test_detach_removes_observer(self):
        library = Library()
        mock_observer = Mock(spec=Notifier)
        library.attach(mock_observer)

        library.detach(mock_observer)

        self.assertNotIn(mock_observer, library._observers)

    def test_add_book_notifies_observers(self):
        mock_observer = Mock(spec=Notifier)
        library = Library()
        library.attach(mock_observer)
        book = Book(
            title="Нова книга",
            author="Автор",
            publication_year=2024,
            isbn="978-0000000001",
            total_copies=1,
        )

        library.add_book(book)

        mock_observer.update.assert_called_once_with(
            "Нова книга доступна - Нова книга"
        )
        self.assertEqual(len(library.catalog.get_all_books()), 1)

    def test_add_book_notifies_all_observers(self):
        mock_observer1 = Mock(spec=Notifier)
        mock_observer2 = Mock(spec=Notifier)
        library = Library()
        library.attach(mock_observer1)
        library.attach(mock_observer2)
        book = Book(
            title="Дизайн-патерни",
            author="Іван Петренко",
            publication_year=2024,
            isbn="978-0000000002",
            total_copies=2,
        )

        library.add_book(book)

        mock_observer1.update.assert_called_once_with(
            "Нова книга доступна - Дизайн-патерни"
        )
        mock_observer2.update.assert_called_once_with(
            "Нова книга доступна - Дизайн-патерни"
        )


if __name__ == "__main__":
    unittest.main()
