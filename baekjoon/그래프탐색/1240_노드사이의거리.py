from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]


def bfs(start, end):
    queue = deque()
    visited = [False] * (n + 1)
    queue.append((start, 0))
    visited[start] = True

    while queue:
        current, distance = queue.popleft()
        if current == end:  # 노드 쌍을 찾은 경우
            return distance  # 출력

        for node, cost in graph[current]:
            if not visited[node]:  # 방문하지 않은 노드
                visited[node] = True
                queue.append((node, distance + cost))  # 노드, 추가된 거리 l큐에 넣기


for _ in range(n - 1):
    n1, n2, dis = map(int, input().split())  # 두 점과 거리
    graph[n1].append((n2, dis))
    graph[n2].append((n1, dis))

for _ in range(m):
    n1, n2 = map(int, input().split())  # 노드 쌍
    print(bfs(n1, n2))
