class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        return f"{self.hour} hours, {self.minute} minutes, {self.second} seconds"

    def add_second(self, n):
        self.second += n
        if self.second > 60:
            self.second = self.second % 60
            self.minute += 1

    def add_minute(self, n):
        self.minute += n
        if self.minute > 60:
            self.minute = self.minute % 60
            self.hour += 1

    def add_hour(self, n):
        self.hour += n
        if self.hour > 24:
            self.hour = self.hour % 24

    def __add__(self, other):
        self.hour += other.hour
        self.minute += other.minute
        self.second += other.second
        if self.second > 60:
            self.second = self.second % 60
            self.minute += 1
        if self.minute > 60:
            self.minute = self.minute % 60
            self.hour += 1
        if self.hour > 24:
            self.hour = self.hour % 24
        return self


# a = Time(1, 10, 45)
# b = Time(3, 55, 6)
# print(a + b)


class Date:

    def __init__(self, day, month, year):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __is_leap_year(self):
        if self.year % 4 == 0:
            return True
        return False

    def add_day(self, n):
        self.day += n
        self.days_to_month()
        self.months_to_year()

    def months_to_year(self):
        if self.month > 12:
            self.month = self.month % 12
            self.year += 1

    def days_to_month(self):
        if self.month == 2:
            if self.__is_leap_year():
                if self.day > 29:
                    self.day = self.day % 29
                    self.month = 3
                elif self.day > 28:
                    self.day = self.day % 29
                    self.month = 3
        elif self.month == 4 or 6 or 9 or 11:
            if self.day > 30:
                self.day = self.day % 30
                self.month += 1
        elif self.month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            if self.day > 31:
                self.day = self.day % 31
                self.month += 1

    def add_month(self, n):
        self.month += n
        self.days_to_month()
        self.months_to_year()

    def add_year(self, n):
        self.year += n


date1 = Date(31, 1, 1980)
date1.add_month(1)


print(date1)