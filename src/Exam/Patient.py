from datetime import datetime, timedelta


class PatientError(Exception):
    pass


class Patient:
    def __init__(self, name: str, surname: str, age: int, gender):
        if age < 18 or age > 100:
            raise PatientError("Not acceptable age for patient")
        if gender != "M" and gender != "F":
            raise PatientError("Not acceptable gender")
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__gender = gender

    def __repr__(self):
        return f"{self.__name} {self.__surname} - {self.__gender}, {self.__age} years old"

    def __ne__(self, other):
        if self.__name == other.__name and self.__surname == other.__surname and \
                self.__age == other.__age and self.__gender == other.__gender:
            return True
        return False


class Doctor:
    def __init__(self, name, surname, schedule: dict):
        self.__name = name
        self.__surname = surname
        self.schedule = schedule  # not private to easily try to change it without getters and setters

    def __repr__(self):
        s = ""
        for k, v in self.schedule.items():
            s += str(k) + ":" + str(v) + "\n"
        return f"Doctor {self.__name} {self.__surname}  schedule \n {s}"

    def register_patient(self, patient: Patient, time: datetime):
        if not self.is_free(time):
            print("Datetime", time, "is already taken from", self.schedule[time], "patient")
        elif self.is_registered(patient):
            print("Patient", patient, "is already registered")
        else:
            self.schedule[time] = patient

    def is_free(self, time: datetime):
        if time.hour < 9 or time.hour > 17:
            return False
        for i in self.schedule.keys():
            if i < time < i + timedelta(minutes=30):
                print("Doctor is not free at", time)
                return False
        return True

    def is_registered(self, patient):
        if patient in self.schedule.values():
            return True
        return False


p1 = Patient("ab", "abyan", 40, "F")
p2 = Patient("ac", "acyan", 30, "M")
p3 = Patient("ad", "adyan", 24, "F")
# print(str(p1))
# print(str(p2))
# patients = [p1, p2, p3]
dt1 = datetime(2023, 1, 5, 14, 30)
dt2 = datetime(2023, 1, 6, 14, 30)
dt3 = datetime(2023, 1, 5, 14, 45)
dt4 = datetime(2023, 1, 5, 16, 45)
# print(dt1)
schedule1 = {dt1: p1, dt2: p2}

d1 = Doctor("Poghos", "Yan", schedule1)

print(d1.is_free(dt4))
print(d1.is_registered(p3))
d1.register_patient(p3, dt4)
print(d1.is_registered(p3))

print(d1.schedule)
