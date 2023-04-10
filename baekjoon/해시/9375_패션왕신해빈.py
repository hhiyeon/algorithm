tc = int(input())
from collections import defaultdict

for _ in range(tc):
    n = int(input())  # 의상의 수
    dict_clothes = defaultdict(list)
    res = 1
    for _ in range(n):
        value, key = map(str, input().split())
        dict_clothes[key].append(value)

    # (a 종류 개수 + 1) * (b 종류 개수 + 1) * ... - 1
    for key in dict_clothes.keys():
        res *= (len(dict_clothes[key]) + 1)

    print(res - 1)
