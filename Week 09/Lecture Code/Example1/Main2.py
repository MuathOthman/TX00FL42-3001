from Book import Book
from Library import Library
from BorrowService import BorrowService

# Create books for Metropolia Myllypuro Library
book1 = Book("Introduction to Algorithms", "Thomas H. Cormen", 123456789)
book2 = Book("Programming Python", "Mark Lutz", 987654321)
book3 = Book("Deep Learning", "Ian Goodfellow", 112233445)

# Create books for Metropolia Karamalmi Library
book4 = Book("You Don’t Know JS", "Kyle Simpson", 223344556)
book5 = Book("Clean Code", "Robert C. Martin", 334455667)
book6 = Book("Design Patterns", "Erich Gamma", 445566778)

# Create libraries
myllypuro_library = Library("Metropolia Myllypuro Library")
karamalmi_library = Library("Metropolia Karamalmi Library")

# Add books to Metropolia Myllypuro Library
myllypuro_library.add_book(book1)
myllypuro_library.add_book(book2)
myllypuro_library.add_book(book3)

# Add books to Metropolia Karamalmi Library
karamalmi_library.add_book(book4)
karamalmi_library.add_book(book5)
karamalmi_library.add_book(book6)

# List books in each library
myllypuro_library.list_books()
print("")
karamalmi_library.list_books()

borrow_service = BorrowService()

borrow_service.borrow_book(myllypuro_library, book1)

myllypuro_library.list_books()