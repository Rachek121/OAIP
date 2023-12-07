num = int(input())
numbers = [int(input()) for e in range(num)]
differences = sorted(set(numbers[i] - numbers[j] for i in range(num) for j in range(num)))
for difference in differences:
    print(difference)
