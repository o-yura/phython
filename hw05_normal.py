# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


import os
import hw05_easy as easy


def change_dir():
    try:
        dir_name = input('Введите папку для перехода:')
        os.chdir(dir_name)
        print('Текущая папка изменена:', dir_name)
    except FileNotFoundError:
        print('Невозможно перейти в папку:', dir_name)
    except Exception as e:
        print(e.__class__)


def list_dir():
    for list in os.listdir():
        print(list)


def r_dir():
    dir_name = input('Введите папку для удаления:')
    easy.remove_dir(dir_name)
    print('Удалена папка:', dir_name)


def c_dir():
    dir_name = input('Введите папку для создания:')
    easy.create_dir(dir_name)
    print('Создана папка:', dir_name)


def user_action(number):
    print('action = ', number)
    if number == 1:
        change_dir()
    if number == 2:
        list_dir()
    if number == 3:
        r_dir()
    if number == 4:
        c_dir()


def start():
    while True:
        choice = int(input('Выберите пункт:\n'
                           '1. Перейти в папку\n'
                           '2. Просмотреть содержимое текущей папки\n'
                           '3. Удалить папку\n'
                           '4. Создать папку\n'
                           '0. Выход\n'
                           '---------------------\n'
                           'Ваш выбор:'))
        if choice == 0:
            break
        else:
            user_action(choice)


start()
