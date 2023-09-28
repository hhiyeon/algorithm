import math


def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())  # 별 개수
point = []
total = 0
parent = [i for i in range(n + 1)]
edges = []


def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


for _ in range(n):
    x, y = input().split()  # x좌표 y좌표
    point.append([float(x), float(y)])

for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = point[i]
        x2, y2 = point[j]
        dis = get_distance(x1, y1, x2, y2)
        edges.append((dis, i, j))

edges.sort()

for cost, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total += cost

answer = "{:.2f}".format(total)
print(answer)
