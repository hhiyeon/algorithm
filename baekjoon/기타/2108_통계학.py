import sys
from collections import Counter
from collections import defaultdict

#n = 5
#arr = [1, 3, 8, -2, 2]
# arr = [-1,-2,-3,-1,-2]
n = int(sys.stdin.readline())
arr = []
dict = defaultdict(int)

for i in range(n):
    a = int(sys.stdin.readline())
    arr.append(a)
    dict[a] = dict.get(a, 0) + 1
res = [0] * 4
sortedArr = sorted(arr)
sortedDict = sorted(dict.items(), key=lambda x: (-x[1], x[0]))
# cntArr = Counter(arr).most_common(2)
# print(dict)
# print(sortedDict)
print(round(sum(arr) / n))
print(sortedArr[int(n // 2)])

if len(arr) > 1:
    if sortedDict[0][1] == sortedDict[1][1]:  # 빈도수가 같을 경우
        print(sortedDict[1][0])
    else:
        print(sortedDict[0][0])
else:
    print(sortedDict[0][0])
print(sortedArr[-1] - sortedArr[0])
