def factorial(adn):
    if adn == 0:
        return 1
    else:
        return adn * factorial(adn - 1)


number = int(input("Введите число: "))
result = factorial(number)
print(f"Факториал числа {number} равен {result}")
