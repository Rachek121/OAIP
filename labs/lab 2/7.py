c = input('Категория >>> ')
if c == 'продукты':
    p = int(input('Цена >>> '))
    if p < 100:
        print('Попробуйте нашу выпечку!')
    if 100 <= p < 500:
        print('Как насчёт орехов в шоколаде?')
    if p > 500:
        print('Попробуйте экзотические фрукты!')
else:
    print('Загляните в товары для дома')