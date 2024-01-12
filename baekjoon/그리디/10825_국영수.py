n = int(input())
array = []

for _ in range(n):
    name, a, b, c = map(str, input().split())
    array.append([name, int(a), int(b), int(c)])

sorted_array = sorted(array, key=lambda x: [-x[1], x[2], -x[3], x[0]])

for info in sorted_array:
    print(info[0])
