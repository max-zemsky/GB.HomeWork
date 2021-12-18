# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное)
# деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого числа.

class Cell:
    def __init__(self, qty):
        self.qty = qty

    def __add__(self, other):
        self.qty = self.qty + other.qty

    def __sub__(self, other):
        result = self.qty - other.qty

        if result < 0:
            print('Операция вычитания не может быть осуществлена!')

        if result > 0:
            self.qty = self.qty - other.qty

    def __mul__(self, other):
        self.qty = self.qty * other.qty

    def __truediv__(self, other):
        self.qty = round(self.qty/other.qty)

    def make_order(self, qty_in_row):
        rows = self.qty // qty_in_row
        cells_uneven = self.qty % qty_in_row

        for i in range(0, rows):
            print('*' * qty_in_row)

        if cells_uneven != 0:
            print('*' * cells_uneven)

cell_one = Cell(15)
cell_two = Cell(12)

#cell_new = Cell(cell_one+cell_two).make_order(5)       Не работает. Пишет "Non-type".

print('Первая клетка: ')
cell_one.make_order(5)

print('Вторая клетка: ')
cell_two.make_order(5)

