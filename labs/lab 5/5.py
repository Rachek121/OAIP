n = int(input('Введите количество флагов: '))
flag = [input('Введите какие будут цвета: ') for i in range(n)]
a = int(input('Количество флагов в гирлянде: '))
d, a2 = divmod(a, n)
print(*(flag * d + flag[:a2]), sep='\n')
