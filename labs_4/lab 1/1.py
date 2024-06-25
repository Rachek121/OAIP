import random

try:
    with open('lines.txt', 'r') as f:
        lines = f.readlines()
        if not lines:
            print("")
        else:
            line = random.choice(lines).strip()
            print(line)
except FileNotFoundError:
    print("Файл не был найден: lines.txt")
