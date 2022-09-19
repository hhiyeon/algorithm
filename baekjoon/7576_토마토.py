from collections import deque

m, n = map(int, input().split())  # 가로, 세로
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
day = 0

# 토마토는 하루가 지날 때 마다 안익은 토마토는 인접한 익은 토마토의 영향을 받아 익게 된다.
# 모든 토마토가 익게 되는 일수 출력, 모두 익지 못하는 상황에는 -1 출력
# 익은 토마토 1, 안익은 토마토 0, 토마토가 없는 경우 -1
# 시작 위치 큐에 넣기
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        px, py = queue.popleft()

        for d in range(4):
            nx = px + dx[d]
            ny = py + dy[d]

            # 토마토가 익지 않았을 경우
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = board[px][py] + 1
                queue.append([nx, ny])


bfs()

# 익지 않은 토마토가 있으면 -1 출력, 모두 다 익은 경우 가장 큰 날짜를 찾아서 출력
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(-1)
            exit(0)
    maxValue = max(board[i])
    day = max(maxValue, day)

# 처음 시작을 1로 했기 때문에 -1
print(day-1)