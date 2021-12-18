# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

print('Введите три числа.')
input_list = []
input_list.append(input('Первое число: '))
input_list.append(input('Второе число: ' ))
input_list.append(input('Третье число: '))

values = []

def check_input(input_list):
    result = True

    for i in range (0, len(input_list)):
        try:
            input_list[i] = float(input_list[i])
            values.append(float(input_list[i]))

        except ValueError:
            print(input_list[i], ' не является числом.')
            print('Пожалуйста, введите 1число!')
            result = False

    return result

def my_func(values):
    sum = 0
    number1 = values[0]
    number2 = values[1]
    min = min(values)
    max = max(values)

    for value in values:
        if value == max:
            sum = max * 2
            return

        if value > min and value < max:
            sum = value + max
            return

        #if value

    # for value in values:
    #     if value > number1:
    #         number1 = value
    #         sum += value
    #         pass
    #
    #     if value > number2:
    #         number2 = value
    #         sum += value
    #         pass
    #
    # if value == 0:
    #     sum = value * 2

    print(sum)

    # ПОЧЕМУ СОРТИРОВКА НЕ РАБОТАЕТ?
    # if check_input(input_list) == True:
    #
    #     input_list.sort(reverse = True)
    #     sum += float(input_list[0]) + float(input_list[1])
    #
    #     print('Сумма наибольших двух аргументов:', sum)


check_input(input_list)
my_func(values)