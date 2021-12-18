# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
#
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    __ASFALT_MASS = 25                  # масса асфальта для 1 кв м на 1 см
    __ASFALT_THICKNESS = 5               # толщина асфальта

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asfalt_count(self):
        asfalt = self._length * self._width *  self.__ASFALT_MASS * self.__ASFALT_THICKNESS / 1000
        num_format = "{:,}".format
        print(num_format(asfalt), 'т')

road = Road(5000, 20)
asfalt = road.asfalt_count()
print(asfalt)