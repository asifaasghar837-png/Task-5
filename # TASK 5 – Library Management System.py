# TASK 5 - Library Management System

class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = True

    def display_book(self):
        status = "Available" if self.available else "Issued"

        print("----------------------------")
        print(f"Book ID   : {self.book_id}")
        print(f"Title     : {self.title}")
        print(f"Author    : {self.author}")
        print(f"Status    : {status}")


# List to store books
books = []


# Add Book
def add_book():
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    book_id = input("Enter Book ID: ")

    # Check duplicate Book ID
    for book in books:
        if book.book_id == book_id:
            print("Book ID already exists!")
            return

    book = Book(title, author, book_id)
    books.append(book)

    print("Book added successfully!")


# View All Books
def view_books():
    if not books:
        print("No books available.")
        return

    print("\n===== All Books =====")

    for book in books:
        book.display_book()


# Search Book
def search_book():
    search = input("Enter Book ID or Title to search: ").lower()

    found = False

    for book in books:
        if book.book_id.lower() == search or book.title.lower() == search:
            book.display_book()
            found = True

    if not found:
        print("Book not found.")


# Issue Book
def issue_book():
    book_id = input("Enter Book ID to issue: ")

    for book in books:
        if book.book_id == book_id:

            if book.available:
                book.available = False
                print("Book issued successfully!")
            else:
                print("Book is already issued.")

            return

    print("Book not found.")


# Return Book
def return_book():
    book_id = input("Enter Book ID to return: ")

    for book in books:
        if book.book_id == book_id:

            if not book.available:
                book.available = True
                print("Book returned successfully!")
            else:
                print("Book is already available.")

            return

    print("Book not found.")


# Delete Book
def delete_book():
    book_id = input("Enter Book ID to delete: ")

    for book in books:
        if book.book_id == book_id:
            books.remove(book)
            print("Book deleted successfully!")
            return

    print("Book not found.")


# Main Menu
while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        delete_book()

    elif choice == "7":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please enter 1-7.")
