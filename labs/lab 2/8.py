p1 = int(input('Цена первого товара:\n>>>'))
p2 = int(input('Цена второго товара:\n>>>'))
p3 = int(input('Цена третьего товара:\n>>>'))
cost = p1 + p2 + p3
if p1 < p2 < p3:
    print('Акция!')
    print('К оплате:', cost / 2)
if p1 > p2 > p3:
    print('Акция!')
    print('К оплате:', cost / 3)
