class Flat:
    def __init__(self, square: float, price: float):
        """
        Создание и подготовка к работе объекта "Квартира"

        :param square: Площадь квартиры (в метрах квадратных)
        :param price: Стоимость квартиры (в млн. рублей)

        Примеры:
        >>> flat = Flat(55.5, 3.5)  # инициализация экземпляра класса
        """
        if not isinstance(square, (int, float)):
            raise TypeError("Площадь квартиры должна быть типа int или float")
        if square <= 0:
            raise ValueError("Площадь квартиры должна быть положительным числом")
        self.square = square

        if not isinstance(price, (int, float)):
            raise TypeError("Стоимость квартиры должна быть int или float")
        if price < 0:
            raise ValueError("Стоимость квартиры не может быть отрицательным числом")
        self.price = price

    def cost_per_one_square(self) -> float:
        """
        Метод, который вычисляет стоимость одного квадратного метра квартиры

        Примеры:
        >>> flat = Flat(55.5, 3.5)
        >>> flat.cost_per_one_square()
        """

    def count_of_rooms(self, count_of_doors: int) -> int:
        """
        Метод, который вычисляет количество комнат в квартире
        :param count_of_doors: Количество дверей в квартире

        Примеры:
        >>> flat = Flat(55.5, 3.5)
        >>> flat.count_of_rooms(3)
        """
        if not isinstance(count_of_doors, (int)):
            raise TypeError("Количество дверей должно быть типа int")
        if count_of_doors < 0:
            raise ValueError("Количество дверей должно быть положительным числом")

class PersonalComputer:
    def __init__(self, motherboard: str, graphic_card: str):
        """
        Создание и подготовка к работе объекта "ПК"

        :param motherboard: Материнская плата компьютера
        :param graphic_card: Видеокарта компьютера

        Примеры:
        >>> PC = PersonalComputer('ASRock H310CM-DVS', 'RTX 4070')  # инициализация экземпляра класса
        """
        if not isinstance(motherboard, (str)):
            raise TypeError("Материнская плата компьютера должна быть типа str")
        self.motherboard = motherboard

        if not isinstance(graphic_card, (str)):
            raise TypeError("Видеокарта компьютера должна быть типа str")
        self.graphic_card = graphic_card

    def is_gaming_PC(self) -> bool:
        """
        Метод, который проверяет является ли ПК игровым

        :return: Является ли компьютер игровым

        Примеры:
        >>> PC = PersonalComputer('ASRock H310CM-DVS', 'RTX 4070')
        >>> PC.is_gaming_PC()
        """

    def add_other_components(self, CPU: str, case: str) -> None:
        """
        Добавление других комплектующих в компьютер
        :param CPU: Центральный процессор
        :param case: корпус ПК

        Примеры:
        >>> PC = PersonalComputer('ASRock H310CM-DVS', 'RTX 4070')
        >>> PC.add_other_components('Intel Core i5-10400F', 'Cougar Duoface RGB')
        """
        if not isinstance(CPU, (str)):
            raise TypeError("Добавляемое название CPU должно быть типа str")
        if not isinstance(case, (str)):
            raise TypeError("Добавляемое название корпуса должно быть типа str")

class ChristmasTree:
    def __init__(self, height: int, origin: str):
        """
        Создание и подготовка к работе объекта "Новогодняя ёлка"

        :param height: Высота ёлки
        :param origin: Происхлждение ёлки

        Примеры:
        >>> tree = ChristmasTree(200, 'Финляндия')  # инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота ёлки должна быть типа int")
        if height <= 0:
            raise ValueError("Высота ёлки должна быть положительным числом")
        self.height = height

        if not isinstance(origin, (str)):
            raise TypeError("Происхлждение ёлки должно быть str")
        self.origin = origin

    def is_tall_tree(self) -> bool:
        """
        Метод, который проверяет является ли ёлка высокой

        :return: Является ли ёлка высокой

        Примеры:
        >>> tree = ChristmasTree(200, 'Финляндия')
        >>> tree.is_tall_tree()
        """

    def remove_tree_height(self, remove_heigt: float) -> None:
        """
        Укоротить ёлку снизу
        :param remove_heigt: Высота спила

        :raise ValueError: Если высота спила превышает саму высоту ёлки, то вызываем ошибку

        Примеры:
        >>> tree = ChristmasTree(200, 'Финляндия')
        >>> tree.remove_tree_height(10)
        """
        if not isinstance(remove_heigt, (int, float)):
            raise TypeError("Высота спила должна быть типа int или float")
        if remove_heigt > self.height:
            raise ValueError("Высота спила превышает саму высоту ёлки")


if __name__ == "__main__":
    import doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации