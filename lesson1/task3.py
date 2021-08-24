"""
3. Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации (нуль
необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону:
“elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
"""

import random


def random_generator(start: int, stop: int) -> (list, dict):
    """

    :param start:
    :param stop:
    :return:
    """
    my_list = []
    if start <= 0:
        start = 1
    for i in range(start, stop + 1):
        my_list.append(random.randint(start, stop))
    my_dict = {f"elem_{x}": y for x, y in zip(range(1, len(my_list) + 1), my_list)}
    return my_list, my_dict


if __name__ == '__main__':
    print(random_generator(1, 5))
