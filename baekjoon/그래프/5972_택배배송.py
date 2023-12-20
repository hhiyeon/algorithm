import heapq
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    arr[a].append((cost, b))
    arr[b].append((cost, a))


def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))
    total = [sys.maxsize] * (n + 1)
    total[1] = 0
    while q:
        cost, node = heapq.heappop(q)
        if node == n:
            return total[node]

        if total[node] < cost:
            continue

        for next_cost, next_node in arr[node]:
            if cost + next_cost < total[next_node]:
                total[next_node] = cost + next_cost
                heapq.heappush(q, (cost + next_cost, next_node))


print(dijkstra())
