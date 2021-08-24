"""4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский, и дочерний классы
получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского класса и функцию
дочернего (функция, отвечающая за отображение информации о товаре в одной строке). """


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
    def get_parent_data(self):
        print(f"Товар название: '{self.name}', цена: {self.price}")


car = ItemDiscountReport()
car.get_parent_data()

car.price = 22500
car.name = 'B-klasse car'
car.get_parent_data()

# Можем поменять и через имя класса:
ItemDiscount.price = 35200
ItemDiscount.name = 'C-Klasse car'
car.get_parent_data()
