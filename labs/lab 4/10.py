s = input('Введите текст: ')
s2 = ''
for i in range(0, len(s), 2):
    if s[i - 1] == ' ':
        s2 += ' '
        s2 += s[i]
        print(s2)
