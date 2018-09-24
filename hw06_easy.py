# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:
    def __init__(self, speed, color, name, is_police):
        print('Создается класс TownCar!')
        self._model = speed
        self._color = color
        self._name = name
        self._is_police = bool(is_police)

    def go(self):
        print('TownCar {} двигается'.format(self._name))

    def stop(self):
        print('TownCar {} останавливается'.format(self._name))

    def turn(self):
        print('TownCar {} поворачивает'.format(self._name))


class SportCar:
    def __init__(self, speed, color, name, is_police):
        print('Создается класс SportCar!')
        self._model = speed
        self._color = color
        self._name = name
        self._is_police = bool(is_police)

    def go(self):
        print('SportCar {} двигается'.format(self._name))

    def stop(self):
        print('SportCar {} останавливается'.format(self._name))

    def turn(self):
        print('SportCar {} поворачивает'.format(self._name))


class WorkCar:
    def __init__(self, speed, color, name, is_police):
        print('Создается класс WorkCar!')
        self._model = speed
        self._color = color
        self._name = name
        self._is_police = bool(is_police)

    def go(self):
        print('WorkCar {} двигается'.format(self._name))

    def stop(self):
        print('WorkCar {} останавливается'.format(self._name))

    def turn(self):
        print('WorkCar {} поворачивает'.format(self._name))


class PoliceCar:
    def __init__(self, speed, color, name, is_police=True):
        print('Создается класс PoliceCar!')
        self._model = speed
        self._color = color
        self._name = name
        self._is_police = bool(is_police)

    def go(self):
        print('PoliceCar {} двигается'.format(self._name))

    def stop(self):
        print('PoliceCar {} останавливается'.format(self._name))

    def turn(self):
        print('PoliceCar {} поворачивает'.format(self._name))


car1 = TownCar('190', 'red', 'Ford', False)
car1.go()
car1.stop()
car1.turn()

car2 = SportCar('220', 'black', 'Audi', False)
car2.go()
car2.stop()
car2.turn()

car3 = WorkCar('60', 'yellow', 'Man', False)
car3.go()
car3.stop()
car3.turn()

car4 = PoliceCar('160', 'white', 'Lada')
car4.go()
car4.stop()
car4.turn()


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, speed, color, name, is_police):
        print('Создается класс Car!')
        self._model = speed
        self._color = color
        self._name = name
        self._is_police = bool(is_police)

    def go(self):
        print('Car {} двигается'.format(self._name))

    def stop(self):
        print('Car {} останавливается'.format(self._name))

    def turn(self):
        print('Car {} поворачивает'.format(self._name))


class WrongCar(Car):
    def service(self):
        print('WrongCar {} в ремонте'.format(self._name))


car5 = WrongCar('0', 'blue', 'Skoda', False)
car5.stop()
car5.service()
