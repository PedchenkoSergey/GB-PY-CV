"""2. Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении
текущей логики работы программы будет сгенерирована ошибка выполнения.
"""


class ItemDiscount:
    __name = "A-klasse car"
    __price = 11700


class ItemDiscountReport(ItemDiscount):
    @staticmethod
    def get_parent_data():
        print(f"Товар название: '{ItemDiscountReport.name}', цена: {ItemDiscountReport.price}")


car = ItemDiscountReport()
car.get_parent_data()
