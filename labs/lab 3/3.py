m = []
while True:
    n = int(input())
    if abs(n) >= 1000:
        break
    m += [n]
print(sorted(set(m))[-2])
