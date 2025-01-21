BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param id_: id книги
        :param name: Название книги
        :param pages: Кол-во страниц
        """
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Определяет поведение функции str(), вызванной для экземпляра класса

        :return: Строка
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Определяет поведение функции repr(), вызыванной для экземпляра класса

        :return: Строка
        """
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'



# TODO написать класс Library
class Library:
    def __init__(self, books=[]):
        """
        Создание и подготовка к работе объекта "Библиотека"

        :param books: Список книг
        """
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку

        :return: Идентификатор последней книги
        """
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_book: int) -> int:
        """
        Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса

        :param id_book: Индекс книги

        :raise ValueError: Если книги нет, то вызвать ошибку ValueError

        :return: Возвращает индекс книги из списка
        """
        for key, value in enumerate(self.books):
            if value.id_ == id_book:
                return key
            else:
                raise ValueError("Книги с запрашиваемым id не существует")



if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
