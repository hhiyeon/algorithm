from collections import deque

n, m = map(int, input().split())  # 세로, 가로
board = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = []  # 넓이를 저장할 리스트


# 그림의 개수, 가장 큰 넓이 출력
# 그림 = 1로 연결된 것,

def bfs(x, y):  # 탐색 위치, 넓이
    # 그림이 시작 하는 위치에서 큐 시작
    board[x][y] = 0  # 현재 위치 방문 체크
    queue = deque()  # 큐 생성
    queue.append([x, y])  # 큐에 해당 칸 넣기
    cnt = 1  # 그림 칸 개수
    while queue:  # 큐가 빌때까지
        a, b = queue.popleft()  # 현재 탐색 위치 제거(탐색 완료)
        for d in range(4):  # 상하좌우 확인
            nx = a + dx[d]
            ny = b + dy[d]
            # 2차원 배열에서 벗어나지 않고, 다음 위치가 1(그림이 있는)인 경우
            if -1 < nx < n and -1 < ny < m and board[nx][ny] == 1:
                board[nx][ny] = 0  # 다음 위치 방문 체크
                queue.append([nx, ny])  # 큐에 탐색할 위치 넣기
                cnt += 1  # 그림 칸 개수
    return cnt


# 그림의 시작점 찾기
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:  # 그림이 있는 위치
            answer.append(bfs(i, j))

if len(answer) == 0: # 그림이 하나도 없는 경우
    print(len(answer))
    print(0)
else:
    print(len(answer))
    print(max(answer))
