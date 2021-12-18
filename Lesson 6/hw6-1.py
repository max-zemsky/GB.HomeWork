# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
# [Maxim] Не понял про усложнение.

import time

class TrafficLight:
    __color = ''
    # colors = ['Red', 'Yellow', 'Green']
    colors = {'Red':7, 'Yellow':2, 'Green':1}

    list(enumerate(colors))

    def __init__(self):
        self.__color = 'Red'

    def stopwatch(seconds):
        start = time.time()
        elapsed = 0
        while elapsed < seconds:
            elapsed = time.time() - start
            print('Seconds count: ', round(elapsed))
            time.sleep(1)

    def running(self):
        for key,value in TrafficLight.colors.items():
            self.__color = key
            print(self.__color)
            self.stopwatch(value)



traffic_light = TrafficLight
traffic_light.running(traffic_light)


