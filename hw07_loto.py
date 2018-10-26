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


### класс работы с мешком
class Bag:

    def __init__(self, name):
        self.name = name
        self._numbers = 0  # количество боченков в мешке

    ### функция наполнения мешка
    def gen(self):
        self.tank = []
        for i in range(1, 91):
            self.tank.append(i)
            self._numbers += 1

    ### вынимаем боченок
    def pull(self):
        try:
            number = random.choice(self.tank)
            self.tank.remove(number)
            self._numbers -= 1
            return number
        except IndexError:
            print('Мешок пуст')


### класс работы с билетами
class Ticket:
    def __init__(self, name):
        self.name = name
        self._numbers = 0  # количество незачеркнутых номеров в билете

    ### генератор номеров билета
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
                    self._numbers += 1
            line = sorted(line)
            line = self._mix_numbers(line)
            self.tank.append(line)

    ### поиск номера в билете
    def search(self, number):
        for line in self.tank:
            for unit in line:
                if number == unit:
                    return True
        return False

    ### зачеркивание номера в билете
    def fix_number(self, number):
        new_tank = []
        for line in self.tank:
            new_line = []
            for unit in line:
                if number == unit:
                    unit = '-'
                    self._numbers -= 1
                new_line.append(unit)
            new_tank.append(new_line)
        self.tank = new_tank

    ### внутренняя функция замешивания номеров в билете
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

    ### вывод билета на экран
    def print_out(self):
        print('Билет игрока: {}, осталось номеров: {}'.format(self.name, self._numbers))
        print('----------------------------------')
        for line in self.tank:
            string = ''
            for unit in line:
                if unit == 0:
                    unit = ' '
                string = string + str(unit) + '\t'
            print(string)
        print('----------------------------------')


### класс игрового процесса
class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        bag1 = Bag('meshok')
        bag1.gen()

        tick1 = Ticket(self.player)
        tick1.gen()

        tick2 = Ticket(self.enemy)
        tick2.gen()

        while True:
            number = bag1.pull()
            if number:
                print('Из мешка вынут боченок: {}. Осталось в мешке - {} '.format(number, bag1._numbers))
                tick1.print_out()
                tick2.print_out()
                print('Введите 1, чтобы зачеркнуть, иначе игра будет продолжена')
                user_in = input('Зачеркнуть или продолжить?:')
                if user_in == '1':
                    if tick1.search(number):
                        tick1.fix_number(number)
                    else:
                        print('Номера в карточке не существует, вы проиграли!')
                        break
                else:
                    if tick1.search(number):
                        print('Пропущен существующий в карточке номер, вы проиграли!')
                        break
                if tick2.search(number):
                    tick2.fix_number(number)
                if tick1._numbers == 0 and tick2._numbers == 0:
                    print('Ничья!')
                    break
                elif tick1._numbers == 0:
                    print('Выиграл игрок', tick1.name)
                    break
                elif tick2._numbers == 0:
                    print('Выиграл игрок', tick2.name)
                    break
            else:
                break


player1 = 'Пользователь'
player2 = 'Компьютер'
game = Game(player1, player2)
game.start()
