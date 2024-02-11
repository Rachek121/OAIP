with open('wares.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    for line in lines:
        if line.startswith('Name;'):
            continue

        data = line.strip().split(';')
        name = data[0]
        old_price = int(data[1])
        new_price = int(data[2])

        if new_price < old_price:
            print(name)
