

class Pizzeria:

    def __init__(self, name, rate, tables):
        self.name = name
        self.rate = rate
        self.tables = tables

    def book(self, tables_need):
        super().__init__()
        print(f'{tables_need} tables were booked in {name}')


class Bot(Pizzeria):

    def __init__(self, tables_need, rate_need):
        super().__init__(name=self.name, tables=self.tables, rate=self.rate)
        self.tables_need = tables_need
        self.rate_need = rate_need

    def search(self, tables_need, rate_need):
        if tables_need <= self.tables & rate_need == self.rate:
            Pizzeria.book()
        elif tables_need > self.tables & rate_need > self.rate:
            print("No available places")
        elif


FirstPizzeria = Pizzeria("Chelentano", 2, 5)
# print(FirstPizzeria.name)

SecondPizzeria = Pizzeria("PizzaBoom", 3, 3)
# print(SecondPizzeria.name)

ThirdPizzeria = Pizzeria("LuxuryPizza", 4, 2)

BestPizzeria = Pizzeria("Just Pizza", 5, 0)

MyBot = Bot("Hello", 3, 3)

MyBot.search(3, 3)











