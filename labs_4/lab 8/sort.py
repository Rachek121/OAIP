sorted_list = sorted([('apple', 3, 'banana'), ('pear', 2, 'orange')], key=lambda x: (x[2], x[1], len(x[0]), -x[1]))
print(sorted_list)