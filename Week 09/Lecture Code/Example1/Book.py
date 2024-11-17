class Book:
    def __init__(self, title, author, ibsn):
        self.title = title
        self.author = author
        self.ibsn = ibsn

    def display(self):
        print("Book Title: " + self.title + " \nAuthor: " + self.author + " \nIBSN: " + str(self.ibsn))
