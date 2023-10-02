import heapq
import sys

input = sys.stdin.readline


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


n, m = map(int, input().split())  # 정점, 간선
edges = []
parent = [i for i in range(n + 1)]
answer = 0
connect = []

for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(edges, (c, a, b))

while edges:
    cost, a, b = heapq.heappop(edges)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer += cost
        connect.append(cost)

answer -= connect.pop()  # 마지막 간선 비용 제거
print(answer)  # 연결 비용 합계
