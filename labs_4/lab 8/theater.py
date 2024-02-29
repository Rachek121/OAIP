def nearby(seats, places=1):
    return list(filter(lambda row: '0'*places in row, seats))

data = [
    "100100011",
    "0001100001",
    "100001001",
    "1110010111"
]

print(*nearby(data, places=4), sep="\n")
