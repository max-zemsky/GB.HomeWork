# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

numbers = [1, 2, 3, 11, 12, 13]
numbers_out = []
sum = 0

file = open("hw5-5-OUT.txt", "w")
for number in numbers:
    str_out = str(number) + ' '
    file.write(str_out)
file.close()

file = open("hw5-5-OUT.txt", "r")
for line in file:
    numbers_out = line.split(' ')


for number in numbers_out:
    if number.isdigit() == False:
        continue

    if number.isdigit() == True:
        sum += int(number)

print(numbers_out)
print(sum)
