from collections import defaultdict
from collections import deque

n = int(input())  # 보드의 크기
k = int(input())  # 사과의 개수

board = [[0] * n for _ in range(n)]  # 정사각 보드
direction = defaultdict(str)

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

queue = deque()
queue.append((0, 0))

for _ in range(k):
    r, c = map(int, input().split())  # 사과의 위치 : 행, 열
    board[r - 1][c - 1] = 2  # 사괴의 위치

L = int(input())  # 뱀의 방향 변환 횟수
for _ in range(L):
    X, C = input().split()  # x 초 뒤에 왼쪽(L), 오른쪽(D) 으로 90도 방향 회전
    direction[int(X)] = C

answer = 0  # 몇 초
nx, ny, d = 0, 0, 0
board[nx][ny] = 1

while True:
    answer += 1  # 1초 증가
    nx += dx[d]
    ny += dy[d]  # 다음 위치

    if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 1:
        # 벽에 부딪 히면 종료 or 뱀 꼬리가 닿는 경우 종료
        break

    if board[nx][ny] == 2:  # 사과가 있는 경우
        board[nx][ny] = 1  # 사과 제거 + 뱀 길이 증가
        queue.append((nx, ny))

    else:  # 사과가 없는 경우
        tail_x, tail_y = queue.popleft()  # 꼬리 위치
        board[tail_x][tail_y] = 0  # 꼬리 칸 비우기
        board[nx][ny] = 1  # 뱀 머리 표시
        queue.append((nx, ny))

    if answer in direction:  # 뱀 방향 정보 중에 해당 시간 이동이 있는 경우
        if direction[answer] == "L":  # 왼쪽 90도 방향
            d = (d - 1) % 4
        else:  # 오른쪽 90도 방향
            d = (d + 1) % 4
print(answer)
