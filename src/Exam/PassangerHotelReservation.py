class Passenger:
    def __init__(self, name: str, city: str, rooms: dict):
        self.__name = name
        self.__city = city
        self.__rooms = rooms

    def __repr__(self):
        return f"{self.__name} {self.__city}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, other):
        self.__name = other.__name

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, other):
        self.__city = other.__city

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, other):
        self.__rooms = other.__roooms


class Hotel:
    def __init__(self, city, rooms):
        self.__city = city
        self.__rooms = rooms

    def __repr__(self):
        return self.__city, self.__rooms

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, other):
        self.__city = other.__city

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, other):
        self.__rooms = other.__rooms

    # geter for the city without decorator
    # def get_city(self):
    #     return self.__city

    def free_rooms_list(self, room_type):
        return self.__rooms[room_type]

    def reserve_rooms(self, room_type, count):
        if self.__rooms[room_type] < count:
            print(" there is not enough rooms to reserve")
        else:
            self.__rooms[room_type] -= count





r = {1: 10, 2: 12, 3:8}

h1 = Hotel("Yerevan", r)

print(h1.free_rooms_list(2))