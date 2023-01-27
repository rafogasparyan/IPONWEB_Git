from src.HW_6.Money import Money
from src.HW_6.Person import Person, PersonError


class DoctorError(Exception):
    pass


class Doctor(Person):

    def __init__(self,  name, surname, gender, age, address, friends, jobs,
                 department: str, profession: str, patronymic: str, salary: Money):
        super(Doctor, self).__init__(name, surname, gender, age, address, friends, jobs)
        self.__department = department
        self.__profession = profession
        self.__patronymic = patronymic
        self.__salary = salary

    def __repr__(self):
        return f"{self.name, self.surname}, {self.__profession, self.__salary}"

    @property
    def department(self):
        return self.__department

    @property
    def profession(self):
        return self.__profession

    @property
    def patronymic(self):
        return self.__patronymic

    @property
    def salary(self):
        return self.__salary

    @department.setter
    def department(self, other):
        self.__department = other

    @profession.setter
    def profession(self, other):
        self.__profession = other

    @patronymic.setter
    def patronymic(self, other):
        self.__patronymic = other

    @salary.setter
    def salary(self, other):
        self.__salary = other


"""
m1 = Money(1000, "USD")

try:
    d = Doctor("a", "a", "a", -10, "a", [], [], "s", "a", "a", m1)
except PersonError as e:
    print(e)


m1 = Money(1000, "USD")

try:
    d = Doctor("a", "a", "a", 11, "a", [], [], "s", "a", "a", m1)
except PersonError as e:
    print(e)

"""