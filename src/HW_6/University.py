from src import City
from src import Date
from src import Person


class University:

    def __init__(self, name: str, founded_at: Date, rector: Person, city: City):
        self.__name = name
        self.__founded_at = founded_at
        self.__rector = rector
        self.__city = city

    def __repr__(self):
        return f"{self.__name, self.__founded_at, self.__rector, self.__city}"

    @property
    def name(self):
        return self.__name

    @property
    def founded_at(self):
        return self.__founded_at

    @property
    def rector(self):
        return self.__rector

    @property
    def city(self):
        return self.__city

    @name.setter
    def name(self, other):
        self.__name = other

    @founded_at.setter
    def founded_at(self, other):
        self.__founded_at = other

    @rector.setter
    def rector(self, other):
        self.__rector = other

    @city.setter
    def city(self, other):
        self.__city = other