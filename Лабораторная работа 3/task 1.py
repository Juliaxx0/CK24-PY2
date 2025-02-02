class Book:
    """
    Базовый класс "Книга"

    :param name: Название книги
    :param author: Автор книги
    """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, author: str) -> None:
        self._author = author

    def __str__(self):
        """
        Определяет поведение функции str(), вызванной для экземпляра класса

        :return: Строка
        """
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        """
        Определяет поведение функции repr(), вызванной для экземпляра класса

        :return: Строка
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """
    Производный класс "Бумажная книга"

    :param pages: Кол-во страниц
    """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError("Кол-во страниц должны быть типа int")
        if  pages <= 0:
            raise ValueError("Кол-во страниц должно быть положительным")
        self._pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """
    Производный класс "Аудиокнига"

    :param duration: Продолжительность аудиокниги
    """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError("Продолжительность аудио должно быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность аудио должно быть положительным")
        self._duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"
