num1 = 1
num2 = 2
search = int(input())
print(num1, num2, end=' ')
while num2 < search:
    print(num2, end=' ')
    num1, num2, = num2, num1 + num2
