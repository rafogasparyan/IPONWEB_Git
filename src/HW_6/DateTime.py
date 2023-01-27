class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __repr__(self):
        return f"{self.__hour}:{self.__minute}:{self.__second}"

    def add_second(self, n):
        self.__second += n
        if self.__second > 60:
            self.__second = self.__second % 60
            self.__minute += 1

    def add_minute(self, n):
        self.__minute += n
        if self.__minute > 60:
            self.__minute = self.__minute % 60
            self.__hour += 1

    def add_hour(self, n):
        self.__hour += n
        if self.__hour > 24:
            self.__hour = self.__hour % 24

    def __add__(self, other):
        seconds1 = self.hour * 3600 + self.minute * 60 + self.second
        seconds2 = other.hour * 3600 + other.minute * 60 + other.second
        sum_seconds = seconds1 + seconds2
        a.__hour = sum_seconds // 3600
        a.__minute = (sum_seconds % 3600) // 60
        a.__second = sum_seconds % 60
        return a

    def __sub__(self, other):
        seconds1 = self.hour * 3600 + self.minute * 60 + self.second
        seconds2 = other.hour * 3600 + other.minute * 60 + other.second
        diff_seconds = abs(seconds1 - seconds2)
        a.__hour = diff_seconds // 3600
        a.__minute = (diff_seconds % 3600) // 60
        a.__second = diff_seconds % 60
        return a
    
    @property
    def hour(self):
        return self.__hour
    
    @property
    def minute(self):
        return self.__minute
    
    @property
    def second(self):
        return self.__second

    @hour.setter
    def hour(self, other):
        self.__hour = other

    @minute.setter
    def minute(self, other):
        self.__minute = other

    @second.setter
    def second(self, other):
        self.__second = other


a = Time(1, 10, 45)
b = Time(3, 55, 45)
print(b - a)


class Date:

    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day

    def __repr__(self):
        return f"{self.__year}-{self.__month}-{self.__day}"

    def is_leap_year(self):
        if self.__year % 4 == 0:
            return True
        return False

    def add_day(self, n):
        self.__day += n
        self.days_to_month()
        self.months_to_year()

    def months_to_year(self):
        if self.month > 12:
            self.__month = self.__month % 12
            self.__year += 1

    def days_to_month(self):
        if self.__month == 2:
            if self.is_leap_year():
                if self.__day > 29:
                    self.__day = self.day % 29
                    self.__month = 3
                elif self.__day > 28:
                    self.__day = self.day % 29
                    self.__month = 3
        elif self.__month == 4 or 6 or 9 or 11:
            if self.__day > 30:
                self.__day = self.__day % 30
                self.__month += 1
        elif self.__month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            if self.__day > 31:
                self.__day = self.day % 31
                self.__month += 1

    def add_month(self, n):
        self.__month += n
        self.days_to_month()
        self.months_to_year()

    def add_year(self, n):
        self.__year += n

    @property
    def year(self):
        return self.__year

    @property
    def month(self):
        return self.__month

    @property
    def day(self):
        return self.__day

    @year.setter
    def year(self, other):
        self.__year = other

    @month.setter
    def month(self, other):
        self.month = other

    @day.setter
    def day(self, other):
        self.__day = other


class DateTime:

    def __init__(self, date: Date, time: Time):
        self.__date = date
        self.__time = time

    def __repr__(self):
        return f"{self.date} {self.time}"

    @property
    def date(self):
        return self.__date

    @property
    def time(self):
        return self.__time

    @date.setter
    def date(self, other):
        self.__date = other

    @time.setter
    def time(self, other):
        self.time = other

    def add_year(self, n):
        self.date.add_year(n)

    def add_day(self, n):
        self.date.add_day(n)

    def add_month(self, n):
        self.date.add_month(n)

    def add_hour(self, n):
        self.time.add_hour(n)

    def add_minute(self, n):
        self.time.add_minute(n)

    def add_second(self, n):
        self.time.add_second(n)

    def sub_year(self, n):
        self.date.year -= n

    def sub_month(self, n):
        m = self.date.month
        m -= n
        if m < 0:
            m += 12
            self.date.year -= 1
        self.date.days_to_month()

    def sub_day(self, n):
        date = self.date
        date.day -= n
        if date.day <= 0:
            if date.month == 3:
                if date.is_leap_year():
                    date.day += 29
                    date.month = 2
                else:
                    date.day += 28
                    date.month = 2
            elif date.month == 5 or 7 or 10 or 12:
                date.day += 30
                date.month -= 1
            elif date.month == 2 or 4 or 6 or 8 or 9 or 11 or 1:
                date.day += 31
                date.month -= 1
                if date.month == 0:
                    self.sub_year(1)
                    self.add_month(12)

    def sub_hour(self, n):
        self.time.hour -= n
        self.__valid_hours()

    def sub_minute(self, n):
        self.time.minute -= n
        self.__valid_minutes()

    def sub_second(self, n):
        self.time.second -= n
        self.__valid_seconds()

    def __valid_hours(self):
        if self.time.hour < 0:
            self.time.hour += 24
            self.sub_day(1)

    def __valid_minutes(self):
        if self.time.minute < 0:
            self.time.hour -= 1
            self.time.minute += 60

    def __valid_seconds(self):
        if self.time.second < 0:
            self.time.second += 60
            self.time.minute -= 1
            self.sub_minute(0)

    def __add__(self, other):
        self.add_second(other.time.second)
        self.add_minute(other.time.minute)
        self.add_hour(other.time.hour)
        self.add_day(other.date.day)
        self.add_month(other.date.month)
        self.add_year(other.date.year)
        return self


"""t = Time(1, 10, 12)
t2 = Time(10, 6, 1)
d2 = Date(10, 7, 2)
d = Date(1995, 8, 1)
dt2 = DateTime(d2, t2)
dt = DateTime(d, t)

dt3 = dt2 + dt
print(dt3)


"""
