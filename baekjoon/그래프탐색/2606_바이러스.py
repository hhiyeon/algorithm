from collections import deque

N = int(input())
V = int(input())
graph = [[] for i in range(N + 1)]  # 2차원 그래프 생성

for _ in range(V):
    u, v = map(int, input().split())
    graph[u].append(v)  # 간선 그래프 만들기
    graph[v].append(u)


def bfs(start):
    cnt = 0
    queue = deque([start])  # 노드 넣을 큐
    # queue.append(start)  # 시작 노드를 큐에 넣기
    visit = [False for _ in range(N + 1)]  # 방문 체크 리스트
    visit[start] = True  # 시작 노드 방문 체크

    while queue:
        temp = queue.popleft()  # 큐에서 노드 하나 꺼내고
        for nx in graph[temp]:  # 노드와 인접한 노드를 찾는다.
            if not visit[nx]:  # 인접한 노드들 중에서, 방문하지 않은 노드 찾기
                queue.append(nx)  # 큐에 노드를 넣고
                visit[nx] = True  # 방문 체크
                cnt += 1
    return cnt


print(bfs(1))
