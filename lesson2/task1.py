"""1. Проверить механизм наследования в Python. Для этого создать два класса. Первый — родительский (ItemDiscount),
должен содержать статическую информацию о товаре: название и цену. Второй — дочерний (ItemDiscountReport),
должен содержать функцию (get_parent_data), отвечающую за отображение информации о товаре в одной строке. Проверить
работу программы, создав экземпляр (объект) родительского класса.

"""


class ItemDiscount:
    name = "A-klasse car"
    price = 11700


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f"Товар название: '{ItemDiscountReport.name}', цена: {ItemDiscountReport.price}")


car = ItemDiscountReport()
car.get_parent_data()
