while True:
    a = int(input())
    if a == 0: break
    if not a % 7 and not a % 3:
        print('Караул!')
    elif not a % 3:
        print('несчасливая')
    elif not a % 7:
        print('опасное')
    else:
        print(a)
