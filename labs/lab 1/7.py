# Подработал над визуалом
while True:
    b = int(input('Введите номер буквы:\n>>>'))
    p = ''
    for i in range(b-1, b+3):
        p += chr(ord('A') + i % 26)
    print('>>>' + p)
