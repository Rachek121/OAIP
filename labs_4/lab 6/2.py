a = [-2, -12, 23, 4, 5, 6, 7, 8, -4, -43, 65]
n = len(a)
for i in range(n-1):
    m = a[i]
    c = i
    for t in range(i+1, n):
        if m > a[t]:
            m = a[t]
            c = t
    if c != i:
        d = a[t]
        a[i] = a[c]
        a[c] = d
print(a)
