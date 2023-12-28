arr = []
n = int(input())

for _ in range(n):
    name, day, month, year = map(str, input().rstrip().split())
    arr.append((int(year), int(month), int(day), name))

arr.sort()
print(arr[-1][3])
print(arr[0][3])
