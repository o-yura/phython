# Правила игры в лото.
#
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
#
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
#
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
#
# --------------------------
# 9 43 62 74 90
# 2 27 75 78 82
# 41 56 63 76 86
# --------------------------
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
#
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
# Если цифра есть на карточке - она зачеркивается и игра продолжается.
# Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# Если цифра есть на карточке - игрок проигрывает и игра завершается.
# Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
#
# Пример одного хода:
#
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
# 6 7 49 57 58
# 14 26 - 78 85
# 23 33 38 48 71
# --------------------------
# -- Карточка компьютера ---
# 7 87 - 14 11
# 16 49 55 88 77
# 15 20 - 76 -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.

import random


class Bag:

    def __init__(self, name):
        self.name = name

    def gen(self):
        self.tank = []
        for i in range(1, 91):
            self.tank.append(i)

    def pull(self):
        try:
            number = random.choice(self.tank)
            self.tank.remove(number)
            return number
        except IndexError:
            print('Мешок пуст')


class Ticket:
    def __init__(self, name):
        self.name = name

    def gen(self):
        self.tank = []
        for i in range(1, 4):
            line = []
            x = 1
            while x < 6:
                number = random.randint(1, 90)
                if not self.search(number) and number not in line:
                    line.append(number)
                    x += 1
            line = sorted(line)
            line = self._mix_numbers(line)
            self.tank.append(line)

    def search(self, number):
        for line in self.tank:
            for unit in line:
                if number == unit:
                    return True
        return False

    def _mix_numbers(self, line):
        new_line = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        indexes = []
        i = 0
        while i < 5:
            index = random.randint(0, 8)
            if index not in indexes:
                indexes.append(index)
                i += 1
        indexes = sorted(indexes)
        i = 0
        for number in line:
            new_line[indexes[i]] = number
            i += 1
        return new_line

    def print_out(self):
        print('Билет игрока:', self.name)
        print('----------------------------------')
        for line in self.tank:
            string = ''
            for unit in line:
                if unit == 0:
                    unit = ' '
                string = string + str(unit) + '\t'
            print(string)
        print('----------------------------------')


bag1 = Bag('meshok')
bag1.gen()

tick1 = Ticket('my')
tick1.gen()
tick1.print_out()

tick2 = Ticket('pc')
tick2.gen()
tick2.print_out()

# print(tick1.search(27))

# while True:
#     number = bag1.pull()
#     if number:
#         print(number)
#     else:
#
#         break
