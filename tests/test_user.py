import os
import sys
import unittest
from unittest.mock import Mock

SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.insert(0, SRC_DIR)

from book import Book
from interfaces import Notifier
from user import Reader


class TestUser(unittest.TestCase):

    def setUp(self):
        self.mock_notifier = Mock(spec=Notifier)
        self.user = Reader(
            "Олена",
            email="olena@example.com",
            max_books=2,
            notifier=self.mock_notifier,
        )
        self.book1 = Book(
            title="Python для всіх",
            author="Чарльз Северенс",
            publication_year=2016,
            isbn="978-0998100670",
            total_copies=1,
        )
        self.book2 = Book(
            title="Clean Code",
            author="Роберт Мартін",
            publication_year=2008,
            isbn="978-0132350884",
            total_copies=1,
        )

    def test_initial_state(self):
        self.assertEqual(self.user.full_name, "Олена")
        self.assertEqual(self.user.max_books, 2)
        self.assertEqual(self.user.status, "active")
        self.assertEqual(len(self.user._borrowed_books), 0)
        self.mock_notifier.update.assert_not_called()

    def test_borrow_book_success_notifies(self):
        result = self.user.borrow_book(self.book1)

        self.assertTrue(result)
        self.assertIn(self.book1, self.user._borrowed_books)
        self.mock_notifier.update.assert_called_once_with(
            "Олена взяла книгу: Python для всіх"
        )

    def test_borrow_book_limit_reached(self):
        self.user.borrow_book(self.book1)
        self.user.borrow_book(self.book2)
        self.mock_notifier.reset_mock()

        extra_book = Book(
            title="Refactoring",
            author="Мартін Фаулер",
            publication_year=1999,
            isbn="978-0201485677",
            total_copies=1,
        )
        result = self.user.borrow_book(extra_book)

        self.assertFalse(result)
        self.assertNotIn(extra_book, self.user._borrowed_books)
        self.mock_notifier.update.assert_not_called()

    def test_borrow_already_borrowed_book(self):
        self.user.borrow_book(self.book1)
        self.mock_notifier.reset_mock()

        result = self.user.borrow_book(self.book1)

        self.assertFalse(result)
        self.assertEqual(len(self.user._borrowed_books), 1)
        self.mock_notifier.update.assert_not_called()

    def test_return_book_success_notifies(self):
        self.user.borrow_book(self.book1)
        self.mock_notifier.reset_mock()

        result = self.user.return_book(self.book1)

        self.assertTrue(result)
        self.assertNotIn(self.book1, self.user._borrowed_books)
        self.mock_notifier.update.assert_called_once_with(
            "Олена повернула книгу: Python для всіх"
        )

    def test_return_book_not_borrowed(self):
        result = self.user.return_book(self.book1)

        self.assertFalse(result)
        self.assertEqual(len(self.user._borrowed_books), 0)
        self.mock_notifier.update.assert_not_called()


if __name__ == "__main__":
    unittest.main()
