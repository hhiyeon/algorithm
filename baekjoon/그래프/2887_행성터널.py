import sys
import heapq

input = sys.stdin.readline


def get_cost(a_point, b_point):
    ax, ay, az = a_point
    bx, by, bz = b_point
    return min(abs(ax - bx), abs(ay - by), abs(az - bz))


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


n = int(input())  # 행성 개수
parent = [i for i in range(n + 1)]
edges = []
points = []

for i in range(n):
    x, y, z = map(int, input().split())  # 행성 좌표
    points.append([x, y, z, i])

for i in range(3):
    points.sort(key=lambda x: x[i])  # x, y, z 각각 정렬
    # print(points)
    for j in range(1, n):
        temp1 = abs(points[j - 1][i] - points[j][i])
        temp2 = points[j - 1][3]
        temp3 = points[j][3]
        # print(temp1, temp2, temp3)
        # cost = get_cost(points[i], points[j])
        heapq.heappush(edges, (temp1, temp2, temp3))

answer = 0

while edges:
    cost, a, b = heapq.heappop(edges)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer += cost

print(answer)
