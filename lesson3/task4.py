"""4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл. Если
файл с таким именем уже существует, выводим соответствующее сообщение. Необходимо открыть файл и подготовить два
списка: с текстовой и числовой информацией. Для создания списков использовать генераторы. Применить к спискам функцию
zip(). Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом, чтобы каждая
строка файла содержала текстовое и числовое значение. Вызвать вторую функцию. В нее должна передаваться ссылка на
созданный файл. Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого. Вся
программа должна запускаться по вызову первой функции. """

import random
import string
import os


def create_txt_file(file_name: str):
    mode = "w"
    if os.path.isfile(file_name):
        mode = input(f'Файл с именем {file_name} уже существует, введите режим работы с файлом:\n'
                     f'"w" - открыть с перезаписью файла\n'
                     f'"a" - дописать в конец файла\n'
                     f'Введите операцию: ')

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
    list_tuples = zip(first_list, second_list)

    with open(file_name, mode) as f:
        for t in list_tuples:
            (x, y) = t
            f.write(str(f"{x}, {y}") + '\n')

    open_txt_file(file_name)


def open_txt_file(file_name: str):
    with open(file_name) as f:
        for l in f.readlines():
            print(l.strip('\n'))


if __name__ == '__main__':
    create_txt_file('task4.txt')
