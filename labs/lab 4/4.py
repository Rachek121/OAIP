l1 = input('Введите букву повтора: ')
n = int(input('Введите количество букв: '))
le = input('Введите буквы для проверки: ')
m = 0
c = 0
for i in range(n):
    if le[i] == l1:
        c += 1
        m = max(m, c)
else:
    c = 0
print(m)
