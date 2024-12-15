# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Cat:
    def __init__(self, name: str, hunger_level: int):
        """
        Создание и подготовка к работе объекта "Кошка"

        :param name: Имя кошки
        :param hunger_level: Уровень голода

        Примеры:
        >>> cat = Cat("Nyusha", 3)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        if not name.isalpha():
            raise ValueError("В имени должны быть только буквы")
        self.name = name

        if not isinstance(hunger_level, int):
            raise TypeError("Уровень голода должен быть типа int")
        if 0 >= hunger_level <= 10:
            raise ValueError("Шкала уровня голода должна быть от 0 до 10")
        self.hunger_level = hunger_level

    def hunger(self) -> None:
        """
        Функция, которая проверяет является ли кошка голодной

        :return: Уровень голода

        Примеры:
        >>> cat = Cat("Nyusha", 3)
        >>> cat.hunger()
        """
        ...

    def play(self) -> None:
        """
        Функция игры с кошкой (Увеличивает уровень голода)

        :return: Уровень голода после игры

        :raise ValueError: Если кошка голодна, то вызываем ошибку

        Примеры:
        >>> cat = Cat("Nyusha", 7)
        >>> cat.play()
        """
        if self.hunger_level < 4:
            raise ValueError(f'{self.name} голодна. Покормите')
        ...

    def feed(self) -> None:
        """
        Функция кормления кошки (Уменьшает уровень голода)

        :return: Уровень голода после кормления

        :raise ValueError: Если кошка не голодна, то вызываем ошибку

        Примеры:
        >>> cat = Cat("Nyusha", 3)
        >>> cat.feed()
        """
        if self.hunger_level > 8:
            raise ValueError(f'{self.name} не голодна')
        ...


class Student:
    def __init__(self, name: str, course: int, list_of_courses: list):
        """
        Создание и подготовка к работе объекта "Студент"

        :param name: Имя студента
        :param course: Номер курса
        :param list_of_courses: Список курсов

        Примеры:
        >>> student = Student("Name", 2, ["Mathematics", "Geometry", "Chemistry"])
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        if not name.isalpha():
            raise ValueError("В имени должны быть только буквы")
        self.name = name

        if not isinstance(course, int):
            raise TypeError("Номер курса должен быть типа int")
        if  not 1 <= course <= 4:
            raise ValueError("Такого курса нет")
        self.course = course

        if not isinstance(list_of_courses, list):
            raise TypeError("Список курсов должен быть типа list")
        self.list_of_courses = list_of_courses

    def information(self) -> None:
        """
        Функция, которая выводит всю информацию о студенте

        :return: Вся информация о студенте

        Примеры:
        >>> student = Student("Name", 2, ["Mathematics", "Geometry", "Chemistry"])
        >>> student.information()
        """
        ...

    def sign_up_for_a_course(self, name_course) -> None:
        """
        Функция, которая добавляет в список новый курс

        :param name_course: Название курса

        Примеры:
        >>> student = Student("Name", 2, ["Mathematics", "Geometry", "Chemistry"])
        >>> student.sign_up_for_a_course("Physics")
        """
        if not isinstance(name_course, str):
            raise TypeError("Название курса должно быть типа str")
        ...


class GroceryBasket:
    def __init__(self, list_products: list[tuple]):
        """
        Создание и подготовка к работе объекта "Продуктовая корзина"

        :param list_products: Список продуктов с их ценой

        Примеры:
        >>> basket = GroceryBasket([("Milk", 50), ("Apple", 15), ("Bread", 25)])
        """

        if not isinstance(list_products, list):
            raise TypeError("Список продуктов должен быть типа list")
        self.list_products = list_products

    def add_products(self, products: tuple[str, int]) -> None:
        """
        :param products: Название продукта и его цена

        Примеры:
        >>> basket = GroceryBasket([("Milk", 50), ("Apple", 15), ("Bread", 25)])
        >>> basket.add_products(("Juice", 20))
        """
        if not isinstance(products, tuple) and not isinstance(products[0], str) and not isinstance(products[1], int):
            raise TypeError("products должен быть типа tuple с название типа str и ценой типа int")
        ...

    def amount_basket(self) -> None:
        """
        Подсчёт суммы всех товаров

        :return: Сумма корзины

        Примеры:
        >>> basket = GroceryBasket([("Milk", 50), ("Apple", 15), ("Bread", 25)])
        >>> basket.amount_basket()
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
