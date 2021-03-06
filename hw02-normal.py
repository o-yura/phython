# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

a1_list1 = [2, -5, 8, 9, -25, 25, 4]
a1_list2 = []

for a1_unit1 in a1_list1:

    if a1_unit1 == abs(a1_unit1):
        a1_sqrt = a1_unit1 ** 0.5

        if a1_sqrt == int(a1_sqrt):
            a1_list2.append(int(a1_sqrt))

print(a1_list2)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

a2_list1 = ['первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое',
            'одинадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое', 'семнадцатое',
            'весемнадцатое', 'девятнадцатое', 'двадцатое', 'тридцатое']
a2_list2 = ['двадцать', 'тридцать']
a2_list3 = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября',
            'декабря']
a2_list4 = []

a2_date = '23.12.2018'

a2_list4 = a2_date.split('.')
a2_day = int(a2_list4[0])
a2_month = int(a2_list4[1])
a2_year = int(a2_list4[2])

if a2_day < 21:
    a2_list4[0] = a2_list1[a2_day - 1]
elif a2_day < 30:
    a2_list4[0] = a2_list2[0] + ' ' + a2_list1[a2_day % 10 - 1]
elif a2_day > 30:
    a2_list4[0] = a2_list2[1] + ' ' + a2_list1[a2_day % 10 - 1]
else:
    a2_list4[0] = a2_list1[20]

a2_list4[1] = a2_list3[a2_month - 1]

print('{} {} {} года'.format(a2_list4[0], a2_list4[1], a2_list4[2], ))

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

a3_list = []
a3_range = 12  # n - элементов
i = 0

while i < a3_range:
    a3_list.append(random.randint(-100, 100))
    i += 1

print(a3_list)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

a4_lst = [1, 2, 4, 5, 6, 2, 5, 2]
a4_lst2 = list(set(a4_lst))

print(a4_lst2)

a4_lst3 = []

for a4_unit in a4_lst:
    a4_count = a4_lst.count(a4_unit)

    if a4_count == 1:
        a4_lst3.append(a4_unit)

print(a4_lst3)
