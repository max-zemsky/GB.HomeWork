goods = []
num = 0
features = {'название':'', 'цена':'', 'кол-вео':'', 'ед. изм.':''}
analytics = {'название':[], 'цена':[], 'кол-вео':[], 'ед. изм.':[]}

while True:
    if input('Для выхода нажмите Q. для продолжения Enter:').upper() == 'Q':
        break

    num += 1
    for f in features.keys():
        prop = input(f'Введите значение свойства {f} - ')
        features[f] = int(prop) if f in ('цена', 'кол-во') else prop
        analytics[f].append(features[f])
    goods.append((num, features.copy()))

    print(f"Структура товаров\n {goods}")
    print(f"Текущая аналитика по товравам:\n")
    print('*' * 30)

    for key,value in analytics.items():
        print(f"{key[:25]:>30}: {value}")

    print('*' * 30)
