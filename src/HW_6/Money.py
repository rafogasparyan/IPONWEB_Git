class MoneyError(Exception):
    pass


class Money:
    exchange = {"AMD": 1, "RUB": 5.8, "USD": 400, "EUR": 430}

    def __init__(self, amount: int, currency: str):
        if amount < 0:
            raise MoneyError("Cannot create Money object with negative amount.")
        self.__amount = amount
        self.__currency = currency

    def __repr__(self):
        return f"{self.__amount} {self.__currency}"

    @property
    def amount(self):
        return self.__amount

    @property
    def currency(self):
        return self.__currency

    @amount.setter
    def amount(self, other):
        self.__amount = other

    @currency.setter
    def currency(self, other):
        self.__currency = other

    def conversation(self, c1):
        ratio = self.exchange[self.__currency] / self.exchange[c1]
        self.__currency = c1
        self.__amount *= ratio

    def __add__(self, other):
        money = self.__amount + other.__amount
        return Money(money, self.__currency)

    def __sub__(self, other):
        money = self.__amount - other.__amount
        return Money(money, self.__currency)

    def __truediv__(self, other):
        money = self.__amount / other.__amount
        return Money(money, self.__currency)

    def __eq__(self, other):
        return self.__currency == other.__currency and self.__amount == other.__amount

    def __ne__(self, other):
        return self.__currency != other.__currency or self.__amount != other.__amount

    def __lt__(self, other):
        return self.__amount < other.__amount

    def __gt__(self, other):
        return self.__amount > other.__amount

    def __le__(self, other):
        return self.__amount <= other.__amount

    def __ge__(self, other):
        return self.__amount >= other.__amount


"""
try:
    m1 = Money(-400, "AMD")
except MoneyError as e:
    print(e)

try:
    m2 = Money(400, "AMD")
except MoneyError as e:
    print(e)


print(m2)
print(m2.amount, "amount")
print(m2.currency, "currency")
try:
    m4 = Money(100, "AMD")
except MoneyError as e:
    print(e)

m3 = m2 + m4

print(m3)
m3.conversation("USD")
print(m3)

"""
