SURNAME = 'Фамилия'
SALARY = 'Оклад'
fields = ('Фамилия', 'Оклад')
person = {'Фамилия': '', 'Оклад': ''}
list_personnel = []
dict = {'Фамилия': ''}

with open('hw5-3.txt', 'r') as file:
    for line in file:
        line = line.removesuffix("\n")
        words = line.split('-')
        #dict[]

        index = 0
        for key in person.keys():
            person[key] = words[index]
            print(words[index])
            index +=1

        #person.update()
        list_personnel.append(person)


#salary_min = float(input('Введите величину минимального оклада: '))



print(list_personnel)