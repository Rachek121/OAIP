total_cost = 0
try:
    with open('prices.txt', 'r') as f:
        for line in f:
            try:
                item, quantity, price = line.strip().split()
                total_cost += float(quantity) * float(price)
            except ValueError:
                print(f"Пропуск строки с ошибкой: {line}")
except FileNotFoundError:
    print("Файл не был найден: prices.txt")
print('{:.2f}'.format(total_cost))
