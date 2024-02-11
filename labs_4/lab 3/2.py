limit = int(input("Введите пороговое значение процента выпускников: "))

with open('vps.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        specialty = data[0]
        correct_summ = data[-1]

        if int(correct_summ) >= limit:
            print(specialty)
