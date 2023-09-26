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


n = int(input())  # 컴퓨터 개수
edges = []
result = 0
parent = [i for i in range(n + 1)]

for i in range(n):
    s = input()

    for j in range(len(s)):
        cost = 0  # 0이면 그대로
        ch = s[j]
        if ch.islower():  # 소문자
            cost = ord(ch) - ord('a') + 1
        elif ch.isupper():
            cost = ord(ch) - ord('A') + 27
        edges.append((cost, i + 1, j + 1))
        result += cost

edges.sort()  # cost 오름차순 정렬

for cost, a, b in edges:
    if cost == 0:
        continue
    if find(parent, a) != find(parent, b):  # 사이클 발생 X
        union(parent, a, b)
        # print(cost)
        result -= cost

flag = True
for i in range(1, n + 1):
    if find(parent, i) != 1:
        flag = False

if flag:
    print(result)
else:
    print(-1)
