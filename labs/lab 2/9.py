a = int(input('Введите число покупателей позавчера:\n>>>'))
b = int(input('Введите число покупателей вчера:\n>>>'))
if b > a:
    print('Сегодня магазин посетит:', b + (b - a), 'человек')
if a > b:
    print('Сегодня магазин посетит:', b - (a - b), 'человек')