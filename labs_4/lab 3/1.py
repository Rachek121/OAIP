with open('wares.csv', 'r', encoding='utf-8') as file:
    lines = sorted(file.readlines(), key=lambda x: float(x.strip().split(';')[1]))
    target = 1001
    result = []

    for line in lines:
        name, price = line.strip().split(';')
        try:
            price = float(price)
        except ValueError:
            print('Ошибка: Некорректное значение цены.')
            exit()

        coust = min(10, int(target // price))

        if coust > 0:
            result.extend([name] * coust)
            target -= coust * price

    if result:
        print(', '.join(result))
    else:
        print('error')
