years = {"Proterozoic": range(635 * 10 ** 6, 2800 * 10 ** 6), "Cenozoic": range(0, 145 * 10 ** 6),
         "Mesozoic": range(145 * 10 ** 6, 300 * 10 ** 6), "Paleozoic": range(300 * 10 ** 6, 635 * 10 ** 6)}
while True:
    x = input('Укажите год: ')
    if x == "":
        break
    x = int(x) * 1000
    for i, val in years.items():
        if x in val:
            print(i)
            break
    else:
        print("Archaea")
