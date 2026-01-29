class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_price(self):
        return sum(p.price for p in self.products)


p1 = Product("Telefon", 3_000_000)
p2 = Product("Quloqchin", 200_000)

order = Order()
order.add_product(p1)
order.add_product(p2)

print("Jami summa:", order.total_price())
