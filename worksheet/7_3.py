class LibraryCatalog:
    def __init__(self, catalog_name):
        self.name = str(catalog_name)

    def add_book(self, title, author):
        self.books.append((str(title), str(author)))

    def remove_book(self, title):
        for book in self.books:
            if title in book[0]:
                self.books.pop()

    def find_books_by_author(self, author):
        books_by_author = []
        for book in self.books:
            if author in book[1]:
                books_by_author.append(book)
        return books_by_author


testcat = LibraryCatalog("text")
testcat.add_book(title="title1", author="author1")
testcat.add_book(title="title3", author="author1")
testcat.add_book(title="title2", author="author2")
print(testcat.books[1])
testcat.remove_book("title2")
print(testcat.books[1])
print(testcat.find_books_by_author("author1"))
