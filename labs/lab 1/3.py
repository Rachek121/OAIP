a = int(input('Введите сумму:\n>>>'))
a1 = a % 1000
a2 = a % 100
a3 = a % 10
a4 = a3 // 1
a5 = a2 // 10
a6 = a1 // 100
a7 = a // 1000
print(a4, '- по 1р')
print(a5, '- по 10р')
print(a6, '- по 100р')
print(a7, '- по 1000р')