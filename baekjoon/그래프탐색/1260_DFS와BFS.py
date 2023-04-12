from collections import deque

N, M, V = map(int, input().split())  # 정점 개수, 간선 개수, 탐색 시작 번호
graph = [[False] * (N + 1) for _ in range(N + 1)]
visit1 = [False for _ in range(N + 1)]
visit2 = [False for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = True
    graph[v][u] = True


def dfs(start):
    visit1[start] = True
    print(start, end=' ')
    for i in range(1, N + 1):  # 시작 노드부터 인접한 노드의 끝(깊이)까지 확인
        if not visit1[i] and graph[start][i]:  # 방문하지 않았고, 간선이 있는 경우
            dfs(i)  # dfs


def bfs(start):
    visit2[start] = True
    queue = deque([start])

    while queue:
        cur = queue.popleft()
        print(cur, end=' ')

        for nx in range(1, N + 1):
            if not visit2[nx] and graph[cur][nx]:  # 방문 체크가 안된 경우와 간선이 이어진 경우
                visit2[nx] = True
                queue.append(nx)


dfs(V)
print()
bfs(V)
