from src.HW_6.DateTime import Date
from src.HW_6.Money import Money
from src.HW_6.Person import Person, Company
from src.HW_6.University import University


class Teacher(Person):

    def __init__(self, university: University, faculty: str, experience: int, start_work_at: Date,
                 subject: str, salary: Money, name, surname, gender, age, address, friends, jobs):
        super(Teacher, self).__init__(name, surname, gender, age, address, friends, jobs)
        self.__university = university
        self.__faculty = faculty
        self.__experience = experience
        self.__start_work_at = start_work_at
        self.__subject = subject
        self.__salary = salary

    def __repr__(self):
        return f"{self.name, self.surname, self.__subject},{self.__experience} years of experience"

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, other):
        self.__experience = other

    @property
    def start_work_at(self):
        return self.__start_work_at

    @start_work_at.setter
    def start_work_at(self, other):
        self.__start_work_at = other

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, other):
        self.__subject = other

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, other):
        self.__faculty = other

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, other):
        self.__salary = other






