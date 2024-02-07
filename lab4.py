class phones():
    """ Базовый класс мобильного телефона """
    def __init__(self, model: str, color: str, display_size: float):
        '''
        Присвоение телефону параметров
        :param model: Модель телефона
        :param color: Цвет телефона
        :param display_size: Размер дисплея

        Примеры:
        >>> phone_A = phones('Iphone11', 'Red', '6.1')
        >>> phone_A.make_call("111-222-7890")
        Calling 111-222-7890...
        '''
        self._model = model
        self._color = color
        self._display_size = display_size

    def make_call(self, number: str) -> None:
        '''
        Сделать звонок на указанный номер
        :param number: Номер телефона, на который будет произведен звонок
        :return: Информация о звонке
        '''
        print(f"Calling {number}...")

    def __str__(self):
        return f"Модель телефона {self._model}. Цвет телефона {self._color}. Размер дисплея {self._display_size}"

    def __repr__(self):
        return f"{slef.__class__.__name__}(model={self._model!r}, color={self._color!r}, display_size={self._display_size!r})"
class iphone(phones):
    """ Класс телефонов на операционной системе iOS """
    def __init__(self, model: str, color: str, display_size: float, version_iOS: float, extension: str):
        '''
        Присвоение телефону на базе операционной системе iOS параметров
        :param model: Модель телефона
        :param color: Цвет телефона
        :param display_size: Размер дисплея
        :param version_iOS: Версия OS
        :param extension: Расширение телефона

        Примеры:
        >>> phone_B = iphone('Iphone11', 'Red', 6.1, 17.04 , 'Pro Max')
        >>> phone_B.make_call("123-456-7890")
        Calling 123-456-7890 via FaceTime...
        '''
        super().__init__(model, color, display_size)
        self._extension = extension
        self._version_OS = version_iOS

    def make_call(self, number: str) -> None:
        '''
        Сделать звонок на указанный номер, используя FaceTime
        :param number: Номер телефона, на который будет произведен звонок
        :return: Информация о звонке
        '''
        print(f"Calling {number} via FaceTime...")  # Перегрузка метода make_call для iOS

    def __str__(self):
        return super().__str__() + f". \nРасширение телефона {self._extension}. Версия операционной системы {self._version_OS}"

    def __repr__(self):
        return f"{self.__class__.__name__}(model={self._model!r}, color={self._color!r}, display_size={self._display_size!r}, version_iOS={self._version_androidOS!r}, extension={self._extension!r})"

class android(phones):
    """ Класс телефонов на операционной системе android """
    def __init__(self, model: str, color: str, display_size: float, version_androidOS: float):
        '''
        Присвоение телефону на базе операционной системе android параметров
        :param model: Модель телефона
        :param color: Цвет телефона
        :param display_size: Размер дисплея
        :param version_androidOS: Версия OS

        Примеры:
        >>> phone_B = android('SumsungS24', 'Black', 6.7, 9.03)
        '''
        super().__init__(model, color, display_size)
        self._version_androidOS = version_androidOS

    def __str__(self):
        return super().__str__() + f". \nВерсия операционной системы {self._version_androidOS}"

    def __repr__(self):
        return f"{self.__class__.__name__}(model={self._model!r}, color={self._color!r}, display_size={self._display_size!r}, version_androidOS={self._version_androidOS!r})"
