a, b, c = map(int, input().split())
s = 0
while True:
    sma, le, he = map(int, input().split())
    if sma == 0 and le == 0 and he == 0:
        break
    s += sma * le * he
    bi = a * b * c
    if s <= bi:
        print("Да")
    else:
        print("Нет")
