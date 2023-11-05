num = int(input('Введите число\n>>>'))
sum1 = sum(range(1, num+1, num % 2 + 1))
print('Сумма делителей равна', num, 'и', sum1)
