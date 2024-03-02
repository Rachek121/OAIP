def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("Введите число: "))
result = factorial(number)
print(f"Факториал числа {number} равен {result}")
