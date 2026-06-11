from abc import ABC, abstractmethod
from typing import List


class Notifier(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass


class BookSearch(ABC):
    @abstractmethod
    def find_by_title(self, title: str) -> List[object]:
        pass

    @abstractmethod
    def find_by_author(self, author: str) -> List[object]:
        pass


class BorrowingRepository(ABC):
    @abstractmethod
    def save(self, borrowing: object) -> None:
        pass

    @abstractmethod
    def get_all(self) -> list:
        pass
