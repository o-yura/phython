# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
from shutil import copyfile

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print('cp <file_name> - создание копии файла')
    print('rm <file_name> - удаление файла')
    print('cd <full_path or relative_path> - перейти в директорию')
    print('ls - показать путь текущей директории')


def make_dir():
    if not unit_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), unit_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(unit_name))
    except FileExistsError:
        print('директория {} уже существует'.format(unit_name))


def ping():
    print("pong")


def copy_file():
    if not unit_name:
        print("Необходимо указать имя файла")
        return
    dir_path = os.path.join(os.getcwd(), unit_name)
    print(dir_path)
    try:
        copy_name = unit_name + '_bkp'
        copyfile(unit_name, copy_name)
        print('Копия файла {} создана'.format(unit_name))
    except FileNotFoundError:
        print('Файла {} не существует'.format(unit_name))


def rem_file():
    if not unit_name:
        print("Необходимо указать имя файла")
        return
    file_name = os.path.join(os.getcwd(), unit_name)

    check_true = input('Вы уверены? (Y/N):')

    if check_true == 'Y' or check_true == 'y':
        try:
            os.remove(file_name)
            print('Файл {} удален'.format(unit_name))
        except FileNotFoundError:
            print('Файла {} не существует'.format(unit_name))
        except IsADirectoryError:
            print('{} не файл, а директория'.format(unit_name))
    else:
        print('Операция отменена')


def goto_dir():
    if not unit_name:
        print("Необходимо указать папку")
        return
    dir_name = os.path.join(os.getcwd(), unit_name)
    try:
        os.chdir(dir_name)
        print('Текущая папка:', os.getcwd())
    except FileNotFoundError:
        print('Папки {} не существует'.format(unit_name))


def list_path():
    print('Текущая папка:', os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    'cp': copy_file,
    'rm': rem_file,
    'cd': goto_dir,
    'ls': list_path
}

try:
    unit_name = sys.argv[2]
except IndexError:
    unit_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
print("Укажите ключ help для получения справки")
