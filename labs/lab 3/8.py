w = input("Введите слово:")
sw = w
while w != "стоп":
    if len(w) < len(sw):
        sw = w
        w = input("Введите слово:")
        print("Самое короткое слово:", sw)
