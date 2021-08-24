"""6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два
класса. Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в первом классе
будет отвечать за вывод названия товара, а вторая — его цены. Далее реализовать выполнение каждой из функции тремя
способами. """


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


class ItemDiscountName(ItemDiscountReport):
    def get_info(self):
        return self.name


class ItemDiscountPrice(ItemDiscountReport):
    def get_info(self):
        return self.price


carA = ItemDiscountReport(0)
carA.get_parent_data()
print(carA)

carB = ItemDiscountName()
print(carB.get_info())

carC = ItemDiscountPrice()
print(carC.get_info())
