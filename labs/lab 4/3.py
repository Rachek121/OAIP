n = int(input("Введите даты вылета\n>>>"))
m = int(input("Введите шаг\n>>>"))
d = ""
for i in range(n, 32, m):
    d += str(i) + " "
print("Возможные даты вылета:" + d)
