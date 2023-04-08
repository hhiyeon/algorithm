# 주식 최대 이익 구하기

tc = int(input())

for _ in range(tc):
    day = int(input())
    cost_list = list(map(int, input().split()))

    total = 0
    max_value = 0
    for idx in range(day - 1, -1, -1):
        if cost_list[idx] > max_value:
            max_value = cost_list[idx]
        else:
            total += max_value - cost_list[idx]
    print(total)
