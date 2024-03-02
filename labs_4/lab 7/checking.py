def checking(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return checking(n, i + 1)


number = 17
if checking(number):
    print(f"{number} - простое число")
else:
    print(f"{number} - составное число")
