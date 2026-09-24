# TASK 5 -- Library Management System

## Objective

Build a console-based Library Management System using Python and
Object-Oriented Programming (OOP).

The purpose of this project is to practice:

-   Classes and Objects
-   `__init__` constructor
-   `self`
-   Methods
-   Lists
-   Loops
-   Conditional Statements
-   Functions
-   Basic OOP

## Features

The Library Management System provides the following options:

1.  Add Book
2.  View All Books
3.  Search Book
4.  Issue Book
5.  Return Book
6.  Delete Book
7.  Exit

## Book Information

Each book contains:

-   Book Title
-   Author
-   Book ID
-   Availability Status

The availability status can be:

-   **Available**
-   **Issued**

## Project Structure

``` text
Task 5/
│
├── library_management.py
└── README.md
```

## How the Program Works

### 1. Add Book

The user enters:

-   Book title
-   Author name
-   Book ID

The system adds the book to the library.

The program also checks whether the Book ID already exists.

### 2. View All Books

Displays all books stored in the library with:

-   Book ID
-   Title
-   Author
-   Availability status

### 3. Search Book

A book can be searched using:

-   Book ID
-   Book Title

### 4. Issue Book

The user enters the Book ID.

If the book is available, its status changes to **Issued**.

If the book is already issued, the system prevents it from being issued
again.

### 5. Return Book

The user enters the Book ID.

If the book is issued, its status changes back to **Available**.

If the book is already available, the system prevents an unnecessary
return.

### 6. Delete Book

The user enters the Book ID and the selected book is removed from the
library.

### 7. Exit

The program displays a thank-you message and closes.

## Class Used

### `Book`

The `Book` class stores the information of each book.

``` python
class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = True
```

## Technologies Used

-   Python 3
-   Object-Oriented Programming
-   Lists
-   Functions
-   Loops
-   Conditional Statements

## How to Run

Open the project folder in VS Code or Terminal.

Run:

``` bash
python3 library_management.py
```

The menu will appear:

``` text
===== Library Management System =====
1. Add Book
2. View All Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Exit
```

Enter a number from **1 to 7** according to the required operation.

## Example

``` text
Enter your choice: 1

Enter Book Title: Python Basics
Enter Author Name: John Smith
Enter Book ID: B001

Book added successfully!
```

Then:

``` text
Enter your choice: 4

Enter Book ID to issue: B001

Book issued successfully!
```

The book status will then show:

``` text
Status: Issued
```

## Learning Outcome

After completing this task, the student will understand how to:

-   Create classes and objects in Python
-   Use constructors with `__init__`
-   Use `self` to access object attributes
-   Create and use methods
-   Store multiple objects in a list
-   Use loops and conditional statements
-   Build a simple console-based management system
-   Manage book availability using OOP

## Advanced Challenge

The project can be extended by adding:

-   File handling to save book records
-   Loading saved records when the program starts
-   Student/member information
-   Tracking which member issued a book
-   Issue date
-   Return date

## Conclusion

The Library Management System is a beginner-friendly Python OOP project
that demonstrates basic library operations through a simple
console-based menu.
