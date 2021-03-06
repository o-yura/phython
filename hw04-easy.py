# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

a1_list1 = [1, 2, 4, 0]
a1_list2 = [i ** 2 for i in a1_list1]
print(a1_list2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

a2_list1 = ['яблоко', 'груша', 'вишня', 'киви', 'виноград', 'черешня']
a2_list2 = ['банан', 'виноград', 'груша', 'апельсин']

a2_list3 = [value for value in a2_list2 if value in a2_list1]
print(a2_list3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
a3_list1 = [0, 3, 5, -5, 3, 6, 87, 12]
a3_list2 = [value for value in a3_list1 if not value % 3 and value > 0 and value % 4]
print(a3_list2)
