from collections import deque
import sys

n = int(sys.stdin.readline())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
arrays = []

for i in range(n):
    arrays.append(list(map(int, sys.stdin.readline().strip())))


def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[-1] * n for _ in range(n)]
    visited[0][0] = 0

    while q:
        x, y = q.popleft()
        if x == n - 1 and y == n - 1:
            return visited[x][y]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if arrays[nx][ny] == 1:
                    q.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


print(bfs())
