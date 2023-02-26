class MyRangeError(Exception):
    pass


class MyRange:

    def __init__(self, current, end, step):
        if (current < end and step < 0) or (current > end and step > 0):
            raise MyRangeError("Impossible to make such range")
        self.__current = current
        self.__end = end
        self.__step = step

    def __repr__(self):
        return f"{self.__current, self.__end, self.__step}"

    def __iter__(self):
        return self

    def __next__(self):
        if (self.__current > self.__end and self.__step > 0) or (self.__current < self.__end and self.__step < 0):
            raise StopIteration
        cur = self.__current
        self.__current += self.__step
        return cur

    def __len__(self):
        return (self.__end - self.__current) // self.__step

    def __getitem__(self, item):
        if item < 0:
            raise ValueError("Negative index can not be found")
        value = self.__current + item * self.__step
        if value > self.__end:
            raise IndexError
        return value

    def __reversed__(self):
        return MyRange(self.__end, self.__current, -self.__step)

"""
try:
    r1 = MyRange(1, 5, 1)
except MyRangeError as e:
    print(e)

for i in r1:
    print(i)


try:
    r2 = MyRange(10, 1, -2)
except MyRangeError as e:
    print(e)

print(next(r2))
print(next(r2))


for i in reversed(r2):
    print(i)
"""

