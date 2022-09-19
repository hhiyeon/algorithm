from collections import deque

n = int(input())
board = [list(map(int, input())) for _ in range(n)]
answer = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 1 집이 있는곳, 0 집이 없는 곳
# 단지 개수, 단지에 속하는 집 개수 출력

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    board[x][y] = 0  # 방문체크
    cnt = 1

    while queue:
        px, py = queue.popleft()

        for d in range(4):
            nx = px + dx[d]
            ny = py + dy[d]

            # 방문 가능한 곳인지 확인
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
                board[nx][ny] = 0  # 다음 방문 체크
                queue.append([nx, ny])  # 큐 입력
                cnt += 1
    return cnt  # 집 개수 출력


for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
for x in answer:
    print(x)
