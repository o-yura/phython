# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

a1_list1 = ["яблоко", "банан", "жорик вартанов", "киви", "груша"]

for a1_num, a1_unit in enumerate(a1_list1):
    print('{0}. {1:>{2}}'.format(a1_num, a1_unit, len(max(a1_list1, key=len))))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

a2_list1 = [1, 2, 'a', 'b', 'cd', 2, 'a', 'ef']
a2_list2 = [2, 3, 'e', 'b', 'cd', 'a']

for a2_unit in a2_list2:
    a2_count = a2_list1.count(a2_unit)

    if a2_count:
        i = 0
        while i < a2_count:
            a2_list1.remove(a2_unit)
            i += 1

print(a2_list1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

a3_list1 = [22, 3, 1, 4, 5, 7, 12, 34]
a3_list2 = []

for a3_unit in a3_list1:
    if a3_unit % 2:
        a3_list2.append(a3_unit * 2)
    else:
        a3_list2.append(a3_unit / 4)

print(a3_list2)
