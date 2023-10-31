n = int(input())
x = input()
r = n
while x != 'стоп':
    if x == '+':
        r += n
    if x == '-':
        r -= n
    n = int(input())
    x = input()
print(r)
