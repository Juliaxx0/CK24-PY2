class Mammals:
    """
    Базовый класс "Млекопитающие"

    :param species: Вид
    :param sound: Издаваемый звук
    :param lifespan: Средняя продолжительность жизни
    """
    def __init__(self, species: str, sound: str, lifespan: int):
        self.species = species #Неизменяемая характеристика животного
        self.sound = sound
        self.lifespan = lifespan

    @property
    def species(self) -> str:
        return self._species

    @species.setter
    def species(self, species: str) -> None:
        self._species = species

    def make_sound(self) -> str:
        """
        Метод, который показывает, какой звук издаёт животное

        :return: Звук животного
        """
        return self.sound

    def describe(self) -> str:
        """
        Метод для описания млекопитающего

        :return: Описание млекопитающего
        """
        return f"Это {self.species}, средняя продолжительность жизни — {self.lifespan} лет."

    def __str__(self) -> str:
        """
        Определяет поведение функции str(), вызванной для экземпляра класса

        :return: Строка
        """
        return f"{self.species!r}: Продолжительность жизни - {self.lifespan} лет, Издаваемый звук - {self.sound!r}"

    def __repr__(self) -> str:
        """
        Определяет поведение функции repr(), вызванной для экземпляра класса

        :return: Строка
        """
        return f"{self.__class__.__name__}(species={self.species!r}, sound={self.sound!r}, lifespan={self.lifespan})"


class DomesticCat(Mammals):
    """
        Дочерний класс "Домашняя кошка"

        :param name: Имя кошки
    """
    def __init__(self,  species: str, sound: str, lifespan: int, name: str):
        super().__init__(species, sound, lifespan)
        self.name = name

    def describe(self) -> str:
        """
        Перегруженный метод для описания млекопитающего

        Причина перегрузки - добавление уникальный информации

        :return: Описание млекопитающего
        """
        return f"Кошка по имени {self.name}. Относится к виду {self.species} и живёт в среднем {self.lifespan} лет"

    def __str__(self) -> str:
        """
        Определяет поведение функции str(), вызванной для экземпляра класса

        Перегрузка метода базового класса

        :return: Строка
        """
        return f"{self.name!r}: Вид - {self.species!r}, Средняя продолжительность жизни - {self.lifespan}, Издаваемый звук - {self.sound!r}"


    def __repr__(self):
        """
        Определяет поведение функции repr(), вызванной для экземпляра класса

        Перегрузка метода базового класса

        :return: Строка
        """
        return f"{self.__class__.__name__}(name={self.name!r}, species={self.species!r}, sound={self.sound!r}, lifespan={self.lifespan})"


if __name__ == "__main__":
    cat = DomesticCat("Felis catus", "Мяу", 30, "Нюша")
    print(cat.describe())
    print(cat.make_sound())
    pass
