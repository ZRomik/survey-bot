from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class AbstractReader(ABC):
    """
    Абстрактный класс описывающий сервис чтения конфигураци
    """
    __source = None
    @property
    def source(self) -> Any:
        """
        Возвращает источник чтения конфигурации
        """
        return self.__source

    @source.setter
    def source(self, value: Any):
        """
        Устанавливает источник чтения конфигурации
        :param value:
        :return:
        """
        self.__source = value

    @abstractmethod
    def load(self):
        self.__config = {}
        """
        Загружает конфигурацию из указанного источника
        """

    @classmethod
    def params(cls, key: str, default):
        """
        Возвращает значение переданного параметра
        :param key: (str) имя параметра
        :return: значение параметра
        """
        return cls.__source.get(key, default)