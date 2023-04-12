from collections import deque

n = int(input())  # 전체 사람의 수
p1, p2 = map(int, input().split())  # 촌수 계산 사람1, 사람2
m = int(input())  # 부모 자식 관계의 개수
graph = [[] for _ in range(n + 1)]
visit = [False for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())  # 부모 자식 관계
    graph[x].append(y)
    graph[y].append(x)


def bfs(start, end):
    queue = deque([(start, 0)])  # (노드, 촌수)
    visit[start] = True

    while queue:
        current, cnt = queue.popleft()  # 노드, 촌수
        if current == end:  # 목표(사람2)에 도달하면 종료
            return cnt
        for nx in graph[current]:
            if not visit[nx]:
                queue.append((nx, cnt + 1))
                visit[nx] = True
    return -1


print(bfs(p1, p2))
