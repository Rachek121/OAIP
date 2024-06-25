from fractions import Fraction
data = [[0, 2, 30, 15], [14, 3, 21, 60], [7, 16, 4, 8]]


def gears(a1, a2, a3):
    for lst1 in a1:
        for el1 in lst1:
            for lst2 in a1:
                for el2 in lst2:
                    if el2 != 0 and Fraction(el1, el2) == Fraction(a2, a3):
                        return el1, el2


print(gears(data, 30, 7))
print(gears(data, 60, 14))
