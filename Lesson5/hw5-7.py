import json
dict = {}                                   # первоначальный словарь
dict_out = {'фирма':'', 'прибыль':int}      # итоговый словарь
profit_average = 0                          # средняя прибыль всех компаний
total_average = {'average_profit':float}    # словарь со средней прибылью всех компаний
list_out = []                               # итоговый список
fields = ('фирма', 'форма собственности', 'выручка', 'издержки')

with open('hw5-7.txt', 'r') as file:
    for line in file:
        parameters = line.split(' ')

        i = 0
        profit = 0
        for parameter in parameters:
            if parameter.__contains__('\n'):
                parameter = parameter.replace('\n','')

            dict[fields[i]] = parameter

            if i == len(fields) - 1:
                profit = float(dict['выручка']) - float(dict['издержки'])

                dict_out['фирма'] = dict['фирма']
                dict_out['прибыль'] = profit
                list_out.append(dict_out)
                print(list_out)

                if profit > 0:
                    profit_average += profit
            i += 1

        # print(dict)
        # print(dict_out)

# Считаем среднюю прибыль
firm_qty =  len(dict.keys()) + 1        # кол-во компаний
profit_average = profit_average / firm_qty
print('Средняя выручка всех компаний: ', profit_average)

total_average['average_profit'] = profit_average

list_out.append(total_average)
print(list_out)


# JSON
with open("hw5-7.json", "w") as write_f:
    json.dump(list_out, write_f)