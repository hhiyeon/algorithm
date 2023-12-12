n = int(input())
numbers = []

for i in range(n):
    number = input()[::-1]
    numbers.append(number)

for idx in range(1, len(numbers[0]) + 1):
    comp = []
    for j in range(n):
        if numbers[j][:idx] in comp:
            break
        comp.append(numbers[j][:idx])
    if len(comp) == n:
        print(idx)
        break
