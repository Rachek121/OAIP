file = open('lines.txt', 'r')
d3 = (file.read())
print("чётные:", d3[::2])
print("нечётные:", d3[1::2])
