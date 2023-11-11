num = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
a = input('Введите число: ')
print('Этих цифр небыло')
print(set(num) - set(map(int, a)))
