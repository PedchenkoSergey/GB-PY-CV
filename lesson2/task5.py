"""5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний
класс. Выполнить перегрузку методов конструктора дочернего класса (метод init, в который должна передаваться
переменная — скидка), и перегрузку метода str дочернего класса. В этом методе должна пересчитываться цена и
возвращаться результат — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать дочерний
и родительский классы (вторая и третья строка после объявления дочернего класса). """


class ItemDiscount:
    __name = "A-klasse car"
    __price = 11700

    @property
    def name(self):
        return ItemDiscount.__name

    @name.setter
    def name(self, name):
        ItemDiscount.__name = name

    @property
    def price(self):
        return ItemDiscount.__price

    @price.setter
    def price(self, price):
        ItemDiscount.__price = price


class ItemDiscountReport(ItemDiscount):

    def __init__(self, discount=0):
        self.discount = discount

    def __str__(self):
        return str(self.price * (1 - self.discount / 100))

    def get_parent_data(self):
        print(f"Товар название: '{self.name}', цена: {self}")


carA = ItemDiscountReport(0)
carA.get_parent_data()
print(carA)

carB = ItemDiscountReport(50)
carB.get_parent_data()
print(carB)

carC = ItemDiscountReport(75)
carC.get_parent_data()
print(carC)

