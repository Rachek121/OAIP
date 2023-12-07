while True:
    try:
        num1 = int(input())
        num2 = int(input())
        result = num1 + num2
    except ValueError:
        print("Ошибка!! \nВведите только целочисленные числа")
    else:
        print(result)
        break
