# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Toy:
    def __init__(self, name, color, type):
        self._name = name
        self._color = color
        self._type = type


class Create_Toy(Toy):

    def purchase(self):
        print('Ведется закупка сырья для', self._name)

    def building(self):
        print('Ведется сборка изделия -', self._name)

    def coloring(self):
        print('Окраска изделия -', self._name)


class Hard_toy(Create_Toy):

    def comp(self):
        print('Ведется обработка пластика, металла', self._name)


class Soft_toy(Create_Toy):

    def comp(self):
        print('Ведется обработка мягкого изделия', self._name)


toy_1 = Soft_toy('bear', 'white', 'soft toy')
toy_1.purchase()
toy_1.comp()
toy_1.building()
toy_1.coloring()
print(type(toy_1))

toy_2 = Hard_toy('train', 'black', 'hard toy')
toy_2.purchase()
toy_2.comp()
toy_2.building()
toy_2.coloring()
print(type(toy_2))
