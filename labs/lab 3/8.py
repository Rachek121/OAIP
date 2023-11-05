w = []
while True:
    w1 = input("Введите слово: ")
    if w1 == 'стоп':
        break
    w.append(w1)
sw = w[0]
for w1 in w:
    if len(w1) < len(sw):
        sw = w1
print('Самое короткое слово:', sw)
