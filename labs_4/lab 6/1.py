ist = [5, 6, 0, 1, 2, 4, 6, 7, 9, 11, 14,]
for i in range(0, 9):
    if ist[i] > ist[i+1]:
        swap = ist[i]
        ist[i] = ist[i+1]
        ist[i+1] = swap
print(ist)
