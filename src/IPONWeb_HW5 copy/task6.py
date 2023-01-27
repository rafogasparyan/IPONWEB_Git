class Company:
    def __init__(self, company_name, founded_at, employees_count):
        self.company_name = company_name
        self.founded_at = founded_at
        self.employees_count = employees_count

    def __repr__(self):
        return f"{self.company_name} was founded at {self.founded_at} and has {self.employees_count} employees"


class Job:
    def __init__(self, company: Company, salary, experience_year, position):
        self.company = company
        self.salary = salary
        self.experience_year = experience_year
        self.position = position

    def __repr__(self):
        return f"In {self.company} company, with salary " \
               f"{self.salary}$, {self.experience_year} experience, as {self.position}"

    def change_salary(self, new_salary):
        self.salary = new_salary

    def change_experience_year(self, experience_year):
        self.experience_year = experience_year

    def change_position(self, new_position):
        self.position = new_position


class Person:
    def __int__(self, name, surname, gender, age, address, friends, jobs):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.address = address
        self.friends = []
        self.jobs = []

    def __repr__(self):
        return f"{self.age} years old {self.gender} {self.name} {self.surname}"

    def add_friend(self, other_person):
        self.friends.append(other_person)

    def remove_friend(self, other):
        self.friends.remove(other)

    def add_job(self, job_title: Job):
        self.jobs.append(job_title)
        job_title.company.employees_count += 1

    def remove_job(self, job_title):
        self.jobs.remove(job_title)
        job_title.company.employees_count -= 1

    def display_job(self):
        return self.jobs

