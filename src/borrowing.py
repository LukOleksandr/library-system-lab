from datetime import date
from typing import List
from interfaces import BorrowingRepository


class Borrowing:
    def __init__(self, reader, book, borrow_date: date, due_date: date):
        self.reader = reader
        self.book = book
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = None
        self.status = "active"

    def close(self, return_date: date) -> None:
        self.return_date = return_date
        self.status = "closed"

    def is_overdue(self, current_date: date) -> bool:
        return (
            self.status == "active"
            and current_date > self.due_date
        )


class InMemoryBorrowingRepository(BorrowingRepository):
    def __init__(self):
        self._borrowings: List[Borrowing] = []

    def save(self, borrowing: Borrowing) -> None:
        self._borrowings.append(borrowing)

    def get_all(self) -> List[Borrowing]:
        return list(self._borrowings)