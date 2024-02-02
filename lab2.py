class Book():
    def __init__(self, id_: int, name: str, pages: int):
        '''
        Присвоение пармаетрам книге
        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book_A = Book(777, "Три товарища", 480)
        '''
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f"Книга {self.name}"

    def __repr__(self) -> str:
        return f"Book({self.id_}, {self.name!r}, {self.pages})"

class Library():
    def __init__(self, books = None):
        '''
        Класс библиотеки
        :param books: Список книг

        Примеры:
        >>> library_A = Library()
        '''
        if books is None:
            books = []
        self.books = books

    def add_new_book(self, book: Book) -> None:
        '''
        Добавление новой книги
        :param book: Новая книга
        :return: Список книг с добавленной новой

        Примеры:
        >>> library_A = Library()
        >>> library_A.add_new_book(Book(777, "Три товарища", 480))
        '''
        self.books.append(book)

    def get_next_book_id(self) -> int:
        '''
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
        :return: Идентификатор для добавления новой книги в библиотеку

        Примеры:
        >>> library_A = Library()
        >>> library_A.add_new_book(Book(777, "Три товарища", 480))
        '''
        if not self.books:
            return 1
        else:
            return self.books[-1].id_ + 1  # Получаем id последней книги и добавляем 1

    def get_index_by_book_id(self, book_id) -> int:
        '''
        Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.
        :param book_id: Индекс книги в списке
        :return: Индекс книги в списке

        Примеры:
        >>> library_A = Library()
        >>> library_A.add_new_book(Book(1, "Три товарища", 480))
        >>> library_A.get_index_by_book_id(1)
        0
        '''
        for index, book in enumerate(self.books):
            if book.id_ == book_id:
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
