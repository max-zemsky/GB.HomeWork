# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.

# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.

from abc import ABC, abstractmethod

class Cloth(ABC):
    @abstractmethod
    def fabric_count(self, size):
        pass

class Coat(Cloth):
    def __init__(self, size):
        self.size = size

    def fabric_count(self):
        return self.size/6.5 + 0.5

class Suit(Cloth):
    def __init__(self, height):
        self.height = height

    def fabric_count(self):
        return 2 * self.height + 0.3

coat = Coat(50)
suit = Suit(187)

print(f'Ткани на пальто понадобится: {coat.fabric_count()}')
print(f'Ткани на костюм понадобится: {suit.fabric_count()}')
