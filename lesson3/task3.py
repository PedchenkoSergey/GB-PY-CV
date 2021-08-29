"""3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором —
значения. Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения,
в словаре для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить. """


import random
import string


def generate_random_string(length: int):
    letters = string.ascii_lowercase
    for _ in range(length):
        yield ''.join(random.choice(letters) for i in range(length))


def generate_random_list(length: int):
    for _ in range(length):
        yield random.randint(0, length)


length_first_list = int(input("Введите количество элементов в первом списке: "))
length_second_list = int(input("Введите количество элементов во втором списке: "))

first_list = list(generate_random_string(length_first_list))
second_list = list(generate_random_list(length_second_list))

if length_second_list < length_first_list:
    for _ in range(length_first_list - length_second_list):
        second_list.append('None')

print(first_list)
print(second_list)
print(dict(zip(first_list, second_list)))
