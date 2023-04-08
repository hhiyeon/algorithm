from collections import deque

n, m = map(int, input().split())  # 가로, 세로
board = [list(map(int, input())) for _ in range(n)]

# 1: 이동할 수 있는 칸, 0: 이동 불가능
# (1,1)에서 출발 (N,M) 위치로 이동할 때 지나야 하는 최소 칸 수 출력

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()  # 큐 생성
    queue.append([x, y])  # 시작점 체크
    while queue:
        a, b = queue.popleft()

        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]

            # 방문 가능한 곳
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                queue.append([nx, ny])  # 큐 삽입
                board[nx][ny] = board[a][b] + 1
    return board[n - 1][m - 1]

print(bfs(0,0))