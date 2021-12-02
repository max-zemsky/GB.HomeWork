import os
lines_number = 0
words_number = 0

with open('hw5-2.txt', 'r') as file:
    for line in file:
        lines_number += 1
        words = line.split()
        words_number = len(words)

        print(f'Кол-во слов в строке №'
              f' {lines_number} - {words_number}')



print(f'Общее кол-во строк в {file.name} - {lines_number}')