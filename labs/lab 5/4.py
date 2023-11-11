# добавил что нужно вводить
number = []
num = int(input('Введите числа: '))
while num != 0:
    number.append(num)
    num = int(input('Введите числа: '))
count = len(number)
a = [num for num in number if num % count == 0]
print(a)
