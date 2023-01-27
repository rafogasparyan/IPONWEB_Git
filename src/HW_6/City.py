from src.HW_6.Person import Person


class CityError(Exception):
    pass


class City:

    def __init__(self, name: str, mayor: Person, population: int, language: str):
        if population < 0:
            raise CityError("Population cna not be negative")
        self.__name = name
        self.__mayor = mayor
        self.__population = population
        self.__language = language

    def __repr__(self):
        return f"mayor of {self.__name} city is {self.__mayor}, has {self.__population} population, and " \
               f"language is {self.__language}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, other):
        self.__name = other

    @property
    def mayor(self):
        return self.__mayor

    @mayor.setter
    def mayor(self, other):
        self.__mayor = other

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, other):
        self.__population = other

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, other):
        self.language = other

"""
try:
    c1 = City("Hoktemberyan", "Vzgo", -1000, "Armenian")
except CityError as e:
    print(e)

try:
    c2 = City("Hoktemberyan", "Vzgo", 11000, "Armenian")
except CityError as e:
    print(e)

print(c2.name)
print(c2.language)
"""