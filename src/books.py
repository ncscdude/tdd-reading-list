class ReadingList:
    def __init__(self):
        self._books = []

    def get_all_books(self):
        return self._books

    def add_book(self, title):
        self._books.append(title)