num1 = int(input())
num2 = int(input())
try:
    result = num1 // num2
except ZeroDivisionError:
    print("Ошибка!! \nДеление на 0 невозможно")
else:
    print(result)
