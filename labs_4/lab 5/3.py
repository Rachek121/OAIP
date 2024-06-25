from collections import deque
line = "1{2 + [3}45 - 6] * (7 - 8) 9"
line2 = "[12 / (9) + 2(5{15 * <2 - 3>}6)]"


def staples(line2):
    a = {']': '[', ')': '(', '}': '{'}
    d = deque()
    for i in line2:
        if i in '[({':
            d.append(i)
        if i in '])}':
            if len(d):
                i = a[i]
                if i != d.pop():
                    return False
            else:
                return False
    if len(d):
        return False
    return True


print(staples(line))
print(staples(line2))
