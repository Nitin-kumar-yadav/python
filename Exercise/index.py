class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []
    
    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)
    
    def showInfo(self):
        print(f"The library has {self.noBooks} books")
    
l1 = Library()
l1.addBook("Harry Potter")
l1.showInfo()