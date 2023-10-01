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


n, p = map(int, input().split())  # 정점, 간선 개수
visit = {}
connect = []
parent = [i for i in range(n + 1)]
min_value = float('inf')
start = 0
answer = 0

for i in range(n):
    c = int(input())  # 방문 비용
    visit[i + 1] = c
    if min_value > c:
        min_value = c
        answer = min_value

# print(visit)

for _ in range(p):
    s, e, l = map(int, input().split())  # s 번째 나라와 e 번쨰 나라 비용 l
    cost = visit[s] + visit[e] + l * 2
    connect.append((cost, s, e))

connect.sort()
# print(connect)
check = 1

for cost, a, b in connect:
    if find(parent, a) != find(parent, b):  # 사이클 X
        union(parent, a, b)
        answer += cost  # 방문 비용 + 연결 비용
        check += 1
        if check == n:
            break
        # print(a, b, cost, answer)

print(answer)

