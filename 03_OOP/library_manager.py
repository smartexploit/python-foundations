"""Library Inventory Manager (Simplified)
Demonstrates Classes, Objects, Instance Attributes, and Methods.
"""

from typing import List


class Book:
    """Represents a single book in the library."""

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_checked_out = False  # Default state: available

    def check_out(self) -> None:
        """Marks the book as checked out if it is available."""
        if self.is_checked_out:
            print(f"[-] '{self.title}' is already checked out.")
        else:
            self.is_checked_out = True
            print(f"[+] Successfully checked out '{self.title}'.")

    def return_book(self) -> None:
        """Marks the book as returned/available."""
        if not self.is_checked_out:
            print(f"[-] '{self.title}' was not checked out.")
        else:
            self.is_checked_out = False
            print(f"[+] Successfully returned '{self.title}'.")

    def display_info(self) -> None:
        """Displays status details of the book."""
        status = "Checked Out" if self.is_checked_out else "Available"
        print(f" • '{self.title}' by {self.author} [{status}]")


class Library:
    """Manages a collection of Book objects."""

    def __init__(self, name: str):
        self.name = name
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        """Adds a Book object to the library collection."""
        self.books.append(book)
        print(f"[+] Added '{book.title}' to {self.name}.")

    def show_all_books(self) -> None:
        """Prints details of all books in the inventory."""
        print(f"\n[ {self.name} Catalog ({len(self.books)} books) ]")
        if not self.books:
            print(" No books currently in library.")
            return

        for book in self.books:
            book.display_info()


def main():
    # Instantiate the Library
    my_library = Library("City Central Library")

    # Instantiate Book objects
    book1 = Book("The Python Workshop", "Andrew Bird")
    book2 = Book("Linux Basics for Hackers", "OccupyTheWeb")

    print("--- 1. Adding Books to Library ---")
    my_library.add_book(book1)
    my_library.add_book(book2)

    print("\n--- 2. Displaying Initial Catalog ---")
    my_library.show_all_books()

    print("\n--- 3. Checking Out a Book ---")
    book1.check_out()

    print("\n--- 4. Catalog After Checkout ---")
    my_library.show_all_books()

    print("\n--- 5. Returning a Book ---")
    book1.return_book()


if __name__ == "__main__":
    main()
