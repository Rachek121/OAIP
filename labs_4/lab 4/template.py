def template(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        per = a + b + c
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        isosceles = a == b or b == c or a == c
        equilateral = a == b and b == c
        print(f"Периметр: {per}")
        print(f"Площадь: {area}")
        print(f"Равнобедренный: {'да' if isosceles else 'нет'}")
        print(f"Равносторонний: {'да' if equilateral else 'нет'}")
    else:
        print("None")


template(5, 4, 5)
template(2, 1, 3)
