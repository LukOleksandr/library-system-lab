from book import Book
from library import Library
from notifications import EmailAlert
from user import Reader, Librarian


def main():
    lib1 = Library(
        "Наукова бібліотека",
        "вул. Шевченка, 10",
    )

    lib2 = Library(
        "Інша бібліотека",
        "вул. Франка, 5",
    )

    print("Перевірка Singleton:")
    print("lib1 is lib2 ->", lib1 is lib2)

    reader1 = Reader("Олена", "olena@example.com")
    reader2 = Reader("Андрій", "andrii@example.com")

    email_alert = EmailAlert("admin@library.com")

    lib1.attach(reader1)
    lib1.attach(reader2)
    lib1.attach(email_alert)

    librarian = Librarian(
        "Ірина Петренко",
        "LIB-001",
    )

    book = Book(
        title="Дизайн-патерни в Python",
        author="Іван Петренко",
        publication_year=2024,
        isbn="948-936-123-41-63",
        total_copies=3,
        genre="Програмування",
    )

    librarian.add_book_to_library(lib1, book)

    lib1.show_books()

    search_service = lib1.get_book_search_service()

    print("\nРезультат пошуку за назвою:")

    for found_book in search_service.find_by_title("Python"):
        print(found_book)


if __name__ == "__main__":
    main()