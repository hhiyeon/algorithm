def find(parent, x):
    if parent[x] != x:  # 루트 노드가 아닌 경우
        return find(parent, parent[x])  # 루트 노드가 나올 때 까지 재귀
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)  # a의 루트 노드
    b = find(parent, b)  # b의 루트 노드

    if a < b:  # a보다 b가 더 큰 경우
        parent[b] = a  # a가 b의 부모
    else:
        parent[a] = b


def is_connected(parent, n): # 각 정점의 부모 확인
    array = set()
    for i in range(1, n + 1):
        array.add(find(parent, i))
        # print(i, array)
    return len(array) == 1


n, m = map(int, input().split())  # 정점, 간선 개수

gender = list(map(str, input().split()))

parent = [i for i in range(n + 1)]
edge = []
answer = 0

for _ in range(m):  # u와 v는 연결, 거리는 d
    u, v, d = map(int, input().split())
    g1, g2 = gender[u - 1], gender[v - 1]
    if g1 != g2:  # 성별이 다를 경우 연결 불가능
        edge.append((d, u, v))

edge.sort()

for cost, a, b in edge:
    if find(parent, a) != find(parent, b):  # 같지 않은 경우
        # print(cost, a, b)
        union(parent, a, b)
        answer += cost

if not is_connected(parent, n):
    print(-1)
else:
    print(answer)
