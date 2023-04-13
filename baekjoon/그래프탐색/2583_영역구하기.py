from collections import deque

m, n, k = map(int, input().split())  # 세로, 가로
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = [[0] * n for _ in range(m)]
answer = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1  # 벽 표시


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    cnt = 1  # 한 좌표에서 시작하는 영역 크기

    while queue:
        node_y, node_x = queue.popleft()

        for d in range(4):
            next_x = node_x + dx[d]
            next_y = node_y + dy[d]
            if 0 <= next_y < m and 0 <= next_x < n and board[next_y][next_x] == 0:
                board[next_y][next_x] = 1  # 영역 방문 표시
                cnt += 1
                queue.append([next_y, next_x])

    return cnt


for i in range(m):
    for j in range(n):
        if board[i][j] == 0:  # 벽이 없는 경우
            board[i][j] = 1
            answer.append(bfs(i, j))
            #print(bfs(i, j))

answer.sort()
print(len(answer))
print(*answer)