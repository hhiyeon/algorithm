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


n, m, k = map(int, input().split())  # 도시 개수, 케이블 수, 발전소 개수
numbers = list(map(int, input().split()))  # 발전소 설치된 도시 번호
parent = [i for i in range(n + 1)]
edges = []
answer = 0

for num in numbers:  # 발전소 설치된 도시의 루트를 0 으로 초기화
    parent[num] = 0

for _ in range(m):
    u, v, w = map(int, input().split())  # u 도시와 v 도시 연결 비용 w
    edges.append((w, u, v))

edges.sort()

for cost, a, b in edges:
    if find(parent, a) != find(parent, b):  # 사이클이 아닌 경우에만 계산
        union(parent, a, b)
        answer += cost

print(answer)
