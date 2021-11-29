# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

print('Введите три числа.')
input_list = []
input_list.append(input('Первое число: '))
input_list.append(input('Второе число: ' ))
input_list.append(input('Третье число: '))

values = []

def check_input(input_list):
    for i in range (0, len(input_list)):
        try:
            input_list[i] = float(input_list[i])
            return True

        except ValueError:
            print(input_list[i], ' не является числом.')
            print('Пожалуйста, введите 1число!')
            return False


def my_func(input_list):
    sum = 0

    if check_input(input_list) == True:

        input_list.sort(reverse = True)
        sum += float(input_list[0]) + float(input_list[1])

        print('Сумма наибольших двух аргументов:', sum)


check_input(input_list)
my_func(input_list)