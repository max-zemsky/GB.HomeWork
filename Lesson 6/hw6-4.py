# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self, speed):
        self.speed = speed
        print(f'{self.name} разгоняется до {self.speed} км/ч.')

    def stop(self):
        self.speed = 0
        print(f'{self.name} остановилась.')

    def turn(self, direction):
        print(f'{self.name} поворачивает {direction}')

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed}.')

class TownCar(Car):
    Car.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} едет со скоростью {self.speed}. {self.name} превышает скорость!')
        else:
            print(f'{self.name} едет со скоростью {self.speed}')


class SportCar(Car):
    Car.is_police = False


class WorkCar(Car):
    Car.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} едет со скоростью {self.speed}. {self.name} превышает скорость!')
        else:
            print(f'{self.name} едет со скоростью {self.speed}')

class PoliceCar(Car):
    Car.is_police = True

sport_car = SportCar(150, 'red', 'Ferrari')
town_car = TownCar(61, 'brown', 'BMW')
work_car = WorkCar(40, 'grey', 'track')
police_car = PoliceCar(70, 'white', 'Mercedes-Benz')

sport_car.show_speed()
town_car.show_speed()
police_car.show_speed()
town_car.stop()

