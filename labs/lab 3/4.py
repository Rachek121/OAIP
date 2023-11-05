n = input('Введите числа: ')
nl = n.split()
nl = [int(num) for num in nl]
s = nl[0]
for i in nl:
    if i < s:
        s = i
print('Наименьшее число:', s)
