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


v, e = map(int, input().split())  # 정점 개수, 간선 개수
parent = [i for i in range(v + 1)]
edges = []

for _ in range(e):
    a, b, c = map(int, input().split())  # a 와 b 정점 가중치 c
    # cost 음수 가능, 절댓값 1,000,000 넘지 않음
    edges.append((c, a, b))

edges.sort()
answer = 0

for cost, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer += cost

print(answer)
