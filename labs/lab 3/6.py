number = 0

for w in range(int(input())+1):
    if len([m for m in range(1, w+1) if w % m == 0]) == 2:
        number += w
print(number)
