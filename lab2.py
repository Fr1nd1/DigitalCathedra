class Book():
    def __init__(self, id: int, name: str, pages: int):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f"Книга {self.name}"

    def __repr__(self) -> str:
        return f"Book({self.id}, {self.name!r}, {self.pages})"

class Library():
    def __init__(self, books = None):
        if books is None:
            books = []
        self.books = books

    def add_new_book(self, book: Book) -> None:
        self.books.append(book)

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1].id + 1  # Получаем id последней книги и добавляем 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == "__main__":
    # Проверка первого пункта лабораторной работы (Класс Книги)
    book_A = Book(777, "Три товарища", 480)
    print(book_A)
    print(repr(book_A))
    # Проверка второго пункта лабораторной работы (Класс Библиотеки)
    library_A = Library()
    library_A.add_new_book(book_A)
    print(library_A.get_next_book_id())
    print(library_A.get_index_by_book_id(777))
