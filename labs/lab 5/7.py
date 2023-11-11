birds = {}
while True:
    line = input('Введите название птиц и их количество: ')
    if line == '':
        break
bird, count = line.split(": ")
count = int(count)
if bird in birds:
    birds[bird] += count
else:
    birds[bird] = count
print(birds)
