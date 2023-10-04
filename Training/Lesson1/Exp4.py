class Book:
    def __init__(self, title, author, pages):
        self.title = title  # Property 1
        self.author = author  # Property 2
        self.pages = pages  # Property 3
        self.is_open = False  # Property 4 (default value)

    def open_book(self):
        self.is_open = True  # Method 1
        return f"The book '{self.title}' is now open."

    def close_book(self):
        self.is_open = False  # Method 2
        return f"The book '{self.title}' is now closed."

    def read_page(self, page_number):
        if self.is_open:
            return f"You're reading page {page_number} of '{self.title}'."
        else:
            return f"Please open the book to read."

# Creating a Book object
book = Book("The Adventures of Alice", "Lewis Carroll", 200)

# Accessing properties
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Number of Pages: {book.pages}\n")

# Calling methods
print(book.open_book())
print(book.read_page(5))
print(book.close_book())
