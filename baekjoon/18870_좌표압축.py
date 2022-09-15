from collections import defaultdict
#n = 5
#arr = [2, 4, -10, 4, -9]
n = int(input())
arr = list(map(int, input().split()))
sortArr = sorted(list(set(arr)))
dict = defaultdict(int)
prev = 0
# print(arr)

for x in sortArr:
    dict[x] = dict.get(x, 1) + prev
    prev = dict[x]

for x in arr:
    print(dict[x] - 1, end=' ')
