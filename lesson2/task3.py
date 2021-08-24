"""3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным. Результат
выполнения заданий 1 и 2 должен быть идентичным.
"""


class ItemDiscount:
    __name = "A-klasse car"
    __price = 11700

    @property
    def name(self):
        return ItemDiscount.__name

    @property
    def price(self):
        return ItemDiscount.__price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f"Товар название: '{self.name}', цена: {self.price}")


car = ItemDiscountReport()
car.get_parent_data()
