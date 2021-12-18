# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# # Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# # Примеры матриц вы найдете в методичке.
# # Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# # Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# # Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

def create_matrix():
    lst_result = []

    for i in range(0, 3):
        lst = []
        for j in range(0, 5):
            lst.append(j)

        lst_result.append(lst)
    print(lst_result)

import random

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __iter__(self):
        return self

    def __str__(self):
        matrix_out = list(self.matrix)

        for row in matrix_out:
            str_out = ''
            for item in row:
                str_out += f'{item} '

            print(str_out)

        return ''       # ВОПРОС!!! Обязательно возвращать строковый результат? Иначе ошибка: returned non-string.

    # Т.к. складывать можно только матрицы с одинаковых размеров, то используется row_stop, column_stop, которые
    # обозначают минимальное кол-во строк и столбцов соответственно.
    def __add__(self, other):
        matrix_sum = []

        j = 0
        row_stop = min(len(self.matrix), len(other.matrix))

        for list_self in self.matrix:
            list_sum = []
            list_other = other.matrix[j]

            column_stop = min(len(list_self), len(other.matrix[j]))

            for i in range(0, column_stop):
                list_sum.append(list_self[i] + list_other[i])
                pass
            matrix_sum.append(list_sum)

            j += 1
            if j == row_stop:
                break

        return Matrix(matrix_sum)


matrix1 = [[31, 22], [37, 43], [51, 86]]
matrix2 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
matrix3 = [[3, 5, 8, 3], [8, 3, 7, 1]]

print(Matrix(matrix1))
print(Matrix(matrix2))
print(Matrix(matrix3))

matrix1_out = Matrix(matrix1)
matrix2_out = Matrix(matrix2)
matrix3_out = Matrix(matrix3)

print('Сумма матрицы 1 и матрицы 2: ')
print(matrix1_out + matrix2_out)

print('Сумма матрицы 2 и матрицы 3: ')
print(matrix2_out + matrix3_out)

print('Сумма матрицы 1 и матрицы 3: ')
print(matrix1_out + matrix3_out)

