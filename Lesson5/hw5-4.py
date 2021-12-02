dict = {'One': 'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
list_out = []

with open('hw5-4.txt', 'r') as file:
    for line in file:
        str_out = line
        line = line.removesuffix("\n")
        line = line.removeprefix(" ")
        words = line.split('-')

        if words[0].__contains__(' '):
            words[0] = words[0].replace(' ', '')
            value_rus = dict[words[0]]
            str_out = str_out.replace(words[0], value_rus)
            list_out.append(str_out)



file_out = open("hw5-4-RUS.txt", "w")
for line in list_out:
    file_out.write(line)
file_out.close()





