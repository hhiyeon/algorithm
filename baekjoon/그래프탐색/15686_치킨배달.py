import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
board = []
house = []
chicken = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

# 0(빈 칸), 1(집), 2(치킨집)
# 도시의 치킨 거리 최솟값 구하기


for i in range(n):
    for j in range(n):
        if board[i][j] == 1:  # 집
            house.append((i, j))
        if board[i][j] == 2:  # 치킨집
            chicken.append((i, j))

combi_chicken = list(combinations(chicken, m))
min_total = float('inf')

for combi in combi_chicken:
    total = 0
    for hx, hy in house:
        min_value = float('inf')
        for j in range(m):
            min_value = min(min_value, abs(combi[j][0] - hx) + abs(combi[j][1] - hy))
        total += min_value
    min_total = min(min_total, total)

print(min_total)
