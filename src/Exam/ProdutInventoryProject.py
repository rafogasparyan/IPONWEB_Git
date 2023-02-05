class ProductException(Exception):
    pass


class Product:
    def __init__(self, price, ID, quantity):
        self.price = price
        self.id = ID
        self.quantity = quantity

    def __repr__(self):
        return f"{self.id} {self.price} {self.quantity}"

    def buy(self, count: int):
        if count > self.quantity:
            raise ProductException("Not so many product to buy")
        self.quantity -= count

    # @staticmethod
    # def get_by_id(id: int, products: list):
    #     for p in products:
    #         if p.id == id:
    #             return p


class Inventory:
    def __init__(self, products):
        self.products = products

    def __repr__(self):
        s = ""
        for p in self.products:
            s += "price - " + str(p.id) + " id - " + str(p.price) + " quantity - " + str(p.quantity) + "\n"
        return s

    def get_by_id(self, id):
        for p in self.products:
            if p.id == id:
                return p

    def sum_of_products(self):
        summ = 0
        for p in self.products:
            summ += p.quantity * p.price
        return summ




p1 = Product(1, 10, 10)
p2 = Product(2, 20, 20)
l = [p1, p2]
i1 = Inventory(l)
print(i1)




