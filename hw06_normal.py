# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:

    def __init__(self, name, health, damage, armor):
        self.name = name
        self._health = health
        self._damage = damage
        self._armor = armor

    def _calc_damage(self, target):
        print('{} атакует {}'.format(self.name, target.name))
        print('Ведется подсчет урона', target.name)
        self._target = target
        new_damage = float(self._damage) / float(target._armor)
        new_health = float(target._health) - new_damage
        target._health = new_health
        print('Остаток здоровья', target.name, target._health)

    def strike(self, target):
        self._target = target
        self._calc_damage(target)


player1 = Person('player1', '100', '10', '8')
player2 = Person('player2', '90', '11', '9')


while True:

    player1.strike(player2)
    if player2._health <= 0:
        print('Победитель: {}, остаток здоровья: {}'.format(player1.name, player1._health))
        break

    player2.strike(player1)
    if player1._health <= 0:
        print('Победитель: {}, остаток здоровья: {}'.format(player2.name, player2._health))
        break