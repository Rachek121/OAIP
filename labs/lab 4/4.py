l1 = input()
n = int(input())
le = input()
m = 0
c = 0
for i in range(n):
    if le[i] == l1:
        c += 1
        m = max(m, c)
else:
    c = 0
print(m)
