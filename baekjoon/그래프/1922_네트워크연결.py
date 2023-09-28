def find(parent, x):
    if parent[x] != x:  # 루트 노드가 아닌 경우
        return find(parent, parent[x])  # 루트 노드를 찾을 때 까지 재귀
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)  # a의 루트 노드
    b = find(parent, b)  # b의 루트 노드
    if a < b:
        parent[b] = a  # a가 더 작으면, b의 부모가 a
    else:
        parent[a] = b


n = int(input())  # 컴퓨터 수
m = int(input())  # 간선 개수
edges = []
parent = [i for i in range(n+1)]
answer = 0

for _ in range(m):  # a와 b를 연결 하는 비용 c
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()  # 오름차순 비용 정렬
# print(edges)

for cost, a, b in edges:
    # print(cost, a, b)
    if find(parent, a) != find(parent, b):  # 사이클이 아닌 경우
        union(parent, a, b)
        answer += cost

print(answer)
