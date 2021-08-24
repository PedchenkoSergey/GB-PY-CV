"""
2. Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):

Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk
нельзя. Данная задача показывает ваше умение работать с
вложенными структурами.
"""
import os


def print_file_dir(file_dir: str, NUM_COUNTS: int = -1) -> None:
    NUM_COUNTS += 1
    tabs = '\t'
    file_name = file_dir.split("\\")[-1]
    print(f'{tabs * NUM_COUNTS}Folder: {file_name}')
    for filename in os.listdir(f"{file_dir}"):
        if os.path.isdir(f'{file_dir}\{filename}'):
            print_file_dir(f'{file_dir}\{filename}', NUM_COUNTS)
        else:
            print(f'{tabs * NUM_COUNTS}\tFile: {filename}')


if __name__ == "__main__":
    print_file_dir(('\\'.join(os.getcwd().split('\\')[0:-2])))
