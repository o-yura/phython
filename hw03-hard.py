# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

print('Задание-1')

# a1_p_name = input('Введите название игрока: ')
# a1_e_name = input('Введите название противника: ')
a1_p_name = 'player'
a1_e_name = 'enemy'
a1_player = dict(name=a1_p_name, health=100, damage=10)
a1_enemy = dict(name=a1_e_name, health=100, damage=7)


def a1_attack(person1, person2):
    damage = person1.get('damage')
    health = person2.get('health') - damage
    person2.update(health)


a1_attack(a1_player, a1_enemy)
a1_attack(a1_enemy, a1_player)

print(a1_player)
print(a1_enemy)

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

print('Задание-2')

path = '/tmp/'

# a2_p_name = input('Введите название игрока: ')
# a2_e_name = input('Введите название противника: ')

a2_p_name = 'player2'
a2_e_name = 'enemy2'

a2_player_raw = dict(name=a2_p_name, health=100, damage=9, armor=1.8)
a2_enemy_raw = dict(name=a2_e_name, health=100, damage=18, armor=1.3)


def a2_create_file(player):
    file = open(path + player.get('name') + '.txt', 'w')

    file.write('health: ' + str(player.get('health')) + '\n')
    file.write('damage: ' + str(player.get('damage')) + '\n')
    file.write('armor: ' + str(player.get('armor')) + '\n')

    file.close


def a2_read_file(player_name):
    player_opts = dict()
    with open(path + player_name + '.txt') as file:
        for line in file:
            values = line.split(': ')
            v_key = values[0]
            v_val = values[1].strip()
            player_opts.update([(v_key, v_val)])
    player_opts.update(name=player_name)
    return (player_opts)


def a2_damage(person1, person2):
    return float(person1.get('damage')) / float(person2.get('armor'))


def a2_attack(person1, person2):
    person2.update(health=float(person2.get('health')) - float(a2_damage(person1, person2)))
    return person2.get('health')


a2_create_file(a2_player_raw)
a2_create_file(a2_enemy_raw)

a2_player = dict(a2_read_file(a2_p_name))
a2_enemy = dict(a2_read_file(a2_e_name))

while True:

    a2_result1 = a2_attack(a2_player, a2_enemy)
    if a2_result1 <= 0:
        print('Победитель: {}, остаток здоровья: {}'.format(a2_p_name, a2_player.get('health')))
        break

    a2_result2 = a2_attack(a2_enemy, a2_player)
    if a2_result2 <= 0:
        print('Победитель: {}, остаток здоровья: {}'.format(a2_e_name, a2_enemy.get('health')))
        break
