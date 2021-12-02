print('Введите данные для записи в файл.\n '
      'Для остановки записи, введите пустую строку.')

file_hw = open('hw5-1.txt', 'w')

while True:
    data = input()

    for line in data:
        file_hw.write(line)

    if data == '':
        break


