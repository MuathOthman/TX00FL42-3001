class BorrowService:
    def borrow_book(self, library, book):
        if book in library.books:
            library.remove_book(book)
        else:
            print("Book not found in the library")
        return library

    def return_book(self, library, book):
        library.add_book(book)
        return library
