import os
import sys
import unittest

SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.insert(0, SRC_DIR)

from book import Book


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book(
            title="1984",
            author="Джордж Орвелл",
            publication_year=1949,
            isbn="978-0451524935",
            total_copies=1,
            genre="Антиутопія",
        )

    def test_initial_state(self):
        self.assertFalse(self.book.is_borrowed)
        self.assertTrue(self.book.is_available())
        self.assertEqual(self.book.title, "1984")
        self.assertEqual(self.book.author, "Джордж Орвелл")
        self.assertEqual(self.book.publication_year, 1949)
        self.assertEqual(self.book.available_copies, 1)

    def test_borrow_success(self):
        result = self.book.borrow()

        self.assertTrue(result)
        self.assertTrue(self.book.is_borrowed)
        self.assertFalse(self.book.is_available())
        self.assertEqual(self.book.available_copies, 0)

    def test_borrow_already_borrowed(self):
        self.book.borrow()

        result = self.book.borrow()

        self.assertFalse(result)
        self.assertTrue(self.book.is_borrowed)
        self.assertEqual(self.book.available_copies, 0)

    def test_return_success(self):
        self.book.borrow()

        result = self.book.return_book()

        self.assertTrue(result)
        self.assertFalse(self.book.is_borrowed)
        self.assertTrue(self.book.is_available())
        self.assertEqual(self.book.available_copies, 1)

    def test_return_not_borrowed(self):
        result = self.book.return_book()

        self.assertFalse(result)
        self.assertFalse(self.book.is_borrowed)
        self.assertTrue(self.book.is_available())


if __name__ == "__main__":
    unittest.main()
