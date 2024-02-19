def func_table(exp, x, y):
    res = [[eval(exp.replace('x', str(i)).replace('y', str(j))) for j in range(y + 1)] for i in range(x + 1)]
    for i in res:
        for j in i:
            print(j, end='\t')
        print()


x = 3
y = 5
func_table('x ** 2 + y', x, y)
