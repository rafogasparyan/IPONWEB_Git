from src import Date
from src import Money
from src import Person
from src import University


class Student(Person):

    def __init__(self, university: University, faculty: str, course: int, started_at: Date, salary: Money,
                 name, surname, gender, age, address, friends, jobs):
        super().__init__(name, surname, gender, age, address, friends, jobs)
        self.__university = university
        self.__faculty = faculty
        self.__course = course
        self.__started_at = started_at
        self.__salary = salary

    # name, surname, gender, age, address, friends, jobs
    def __repr__(self):
        return f"{self.name} {self.surname} {self.__university} university, {self.__faculty} faculty"

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, other):
        self.__university = other

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, other):
        self.__faculty = other

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, other):
        self.__course = other

    @property
    def started_at(self):
        return self.__started_at

    @started_at.setter
    def started_at(self, other):
        self.__started_at = other

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, other):
        self.__salary = other



