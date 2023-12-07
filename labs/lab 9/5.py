try:
    num1 = int(input())
    num2 = int(input())
    result = num1 // num2
except ZeroDivisionError:
    print("Ошибка!! \nДеление на 0 невозможно")
except ValueError:
    print("Ошибка!! \nВведите только целочисленные числа")
else:
    print(result)
finally:
    print("Выход из системы!!")
