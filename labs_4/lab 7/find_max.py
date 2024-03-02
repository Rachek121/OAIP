def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_length = find_max(lst[1:])
        return lst[0] if lst[0] > max_length else max_length


numbers = [3, 7, 2, 10, 5]
print(f"Максимальное число в списке: {find_max(numbers)}")
