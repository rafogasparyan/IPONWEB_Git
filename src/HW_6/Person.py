class Company:
    def __init__(self, company_name, founded_at, employees_count):
        self.__company_name = company_name
        self.__founded_at = founded_at
        self.__employees_count = employees_count

    def __repr__(self):
        return f"{self.__company_name} was founded at {self.__founded_at} and has {self.__employees_count} employees"

    @property
    def company_name(self):
        return self.__company_name

    @property
    def founded_at(self):
        return self.__founded_at

    @property
    def employees_count(self):
        return self.__employees_count

    @company_name.setter
    def company_name(self, other):
        self.__company_name = other

    @founded_at.setter
    def founded_at(self, other):
        self.__founded_at = other

    @employees_count.setter
    def employees_count(self, other):
        self.__employees_count = other


class Job:
    def __init__(self, company: Company, salary, experience_year, position):
        self.__company = company
        self.__salary = salary
        self.__experience_year = experience_year
        self.__position = position

    def __repr__(self):
        return f"In {self.__company} company, with salary " \
               f"{self.__salary}$, {self.__experience_year} experience, as {self.__position}"

    @property
    def company(self):
        return self.__company

    @property
    def salary(self):
        return self.__salary

    @property
    def experience_year(self):
        return self.__experience_year

    @property
    def position(self):
        return self.__position

    @company.setter
    def company(self, other):
        self.__company = other

    @salary.setter
    def salary(self, other):
        self.__salary = other

    @experience_year.setter
    def experience_year(self, other):
        self.__experience_year = other

    @company.setter
    def company(self, other):
        self.__company = other


class PersonError(Exception):
    pass


class Person:

    def __init__(self, name, surname, gender, age, address, friends: list, jobs: list):
        if age < 0:
            raise PersonError("Age can not be negative number")
        self.__name = name
        self.__surname = surname
        self.__gender = gender
        self.__age = age
        self.__address = address
        self.__friends = friends
        self.__jobs = jobs

    def __repr__(self):
        return f"{self.__age} years old {self.__gender} {self.__name} {self.__surname}"

    def add_friend(self, other_person):
        self.__friends.append(other_person)

    def remove_friend(self, other):
        self.__friends.remove(other)

    def add_job(self, job_title: Job):
        self.__jobs.append(job_title)
        job_title.company.employees_count += 1

    def remove_job(self, job_title):
        self.__jobs.remove(job_title)
        job_title.company.employees_count -= 1

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def gender(self):
        return self.__gender

    @property
    def age(self):
        return self.__age

    @property
    def address(self):
        return self.__address

    @property
    def friends(self):
        return self.__friends

    @property
    def jobs(self):
        return self.__jobs

    @name.setter
    def name(self, other):
        self.__name = other

    @surname.setter
    def surname(self, other):
        self.__surname = other

    @gender.setter
    def gender(self, other):
        self.__gender = other

    @age.setter
    def age(self, other):
        self.__age = other

    @address.setter
    def address(self, other):
        self.__address = other

    @friends.setter
    def friends(self, other):
        self.__friends = other

    @jobs.setter
    def jobs(self, other):
        self.__jobs = other




