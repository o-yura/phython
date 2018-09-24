# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

from os import mkdir, rmdir, listdir, path


def create_dir(dir_name):
    try:
        mkdir(dir_name)
    except FileExistsError:
        print('Папка уже существует:', dir_name)
    except Exception as e:
        print(e.__class__)


def remove_dir(dir_name):
    try:
        rmdir(dir_name)
    except FileNotFoundError:
        print('Папки не существует:', dir_name)
    except Exception as e:
        print(e.__class__)


if __name__ == '__main__':
    for i in range(1, 10):
        create_dir('dir_' + str(i))

    for i in range(1, 10):
        remove_dir('dir_' + str(i))

    # Задача-2:
    # Напишите скрипт, отображающий папки текущей директории.

if __name__ == '__main__':
    for name in listdir():
        if path.isdir(name):
            print(name)

    # Задача-3:
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

if __name__ == '__main__':
    from shutil import copyfile

    a3_name = (__file__)
    a3_copy = a3_name + '_bkp'
    copyfile(a3_name, a3_copy)
