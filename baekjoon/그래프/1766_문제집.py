import heapq
import sys

input = sys.stdin.readline
n, m = map(int, input().split())  # 문제의 수, 정보 개수
heap = []
InDegree = [0] * (n + 1)
graph = [[] for i in range(n + 1)]
arr = []
answer = []

for _ in range(m):
    a, b = map(int, input().split())  # 정수 순서 쌍
    # a 보다 b가 쉬움
    graph[a].append(b)
    InDegree[b] += 1

for i in range(1, n + 1):
    if InDegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    top = heapq.heappop(heap)
    for b in graph[top]:
        InDegree[b] -= 1
        if InDegree[b] == 0:
            heapq.heappush(heap, b)
    answer.append(top)

print(*answer)
