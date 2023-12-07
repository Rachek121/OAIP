numbers = [1, 2, 3, 4, 5, 6, 11, 32, 43, ]
search = 11
variable = 0
checking = len(numbers) - 1
coust = (variable + checking) // 2
while search != numbers[coust]:
    if search > numbers[coust]:
        variable = coust + 1
    else:
        checking = coust - 1
    coust = (variable + checking) // 2
print(coust)
