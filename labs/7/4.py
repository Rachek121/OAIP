num1 = 1
num2 = 100
while True:
    variable = num1 % num2
    print(num1, variable)
    if variable < num1:
        print(num1 - variable)
        break
    else:
        num1 *= 2
