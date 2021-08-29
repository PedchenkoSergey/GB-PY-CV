"""5. Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений
заменить на значения типа example345 (строка+число). Далее — усовершенствовать вторую функцию из предыдущего примера
(функцию извлечения данных). Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
вывод первого вхождения, вывод всех вхождений. Реализовать замену всех найденных подстрок на новое значение и вывод
всех подстрок, состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, example345. """

import random
import string
import os
import re


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
            f.write(str(f"{x}{y}") + '\n')
            f.write(str(f"example{y}") + '\n')

    open_txt_file(file_name)


def open_txt_file(file_name: str):
    regex = re.compile(r'example')
    with open(file_name) as f:
        for l in f.readlines():
            print(l.strip('\n'))
            if regex.search(l):
                print(f"ИЗМЕННЕННАЯ СТРОКА: {regex.sub('primer', l)}", end='')


if __name__ == '__main__':
    create_txt_file('task5.txt')
