import heapq
import sys
input = sys.stdin.readline
#V, E = 5, 6  # 정점의 개수, 간선의 개수
V, E = map(int, input().split())
K = int(input())
#k = 1  # 시작 정점의 번호
inf = float('inf')
graph = [[] for _ in range(V + 1)]
distance = [inf]*(V+1) # 가중치 테이블 dp
pq = []  # 우선순위 큐

for _ in range(E):
    u, v, w = map(int, input().split())  # u에서 v로 가는 가중치 w 간선
    graph[u].append((v, w))

def dijkstra(start):
    distance[start] = 0
    heapq.heappush(pq, [0, start])  # 거리, 시작 정점 번호

    while pq: # 우선순위 큐를 사용해서 가장 최단 거리의 노드 고르기
        dist, now = heapq.heappop(pq)

        # 현재 노드가 이미 방문된 기록이 있으면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]: # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost # 가중치르 갱신 해준다.
                heapq.heappush(pq, [cost, i[0]])

dijkstra(K)

for i in distance[1:]:
    if i == inf:
        print("INF")
    else:
        print(i)