a = [int(input('')) for i in range(int(input('Введите сколько будет чисел, а затем сами числа = ')))]
print(len(set(''.join(map(str, a)))))
