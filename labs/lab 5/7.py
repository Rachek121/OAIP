birds = {}
while True:
    observation = input()
    if observation == '':
        print(birds)
        break
    bird, count = observation.split(": ")
    if bird in birds:
        birds[bird] += int(count)
    else:
        birds[bird] = int(count)
