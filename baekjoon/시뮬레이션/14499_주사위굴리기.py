# 세로, 가로 크기, 좌표 x, y, 명령의 개수 k
n, m, x, y, k = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

# 이동 순서 : 동 1, 서 2, 북 3, 남 4
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
order_list = list(map(int, input().split()))
dice = [0] * 6
nx, ny = x, y


def get_dice(d):
    global dice
    d1, d2, d3, d4, d5, d6 = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if d == 1:  # 동
        return [d4, d2, d1, d6, d5, d3]
    elif d == 2:  # 서
        return [d3, d2, d6, d1, d5, d4]
    elif d == 3:  # 북
        return [d5, d1, d3, d4, d6, d2]
    else:  # 남
        return [d2, d6, d3, d4, d1, d5]


for order in order_list:
    nx = x + dx[order - 1]
    ny = y + dy[order - 1]

    # 범위 넘어 가면 패스
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    dice = get_dice(order)

    # 주사위 윗면 숫자 출력
    if board[nx][ny] == 0:  # 이동 칸이 0이면, 주사위 바닥의 값 복사
        board[nx][ny] = dice[5]  # d6 = dice[5]
    else:  # 0이 아니면, 칸에 쓰여 있는 수가 주사위 바닥 면에 복사, 칸 수는 0 으로
        dice[5] = board[nx][ny]
        board[nx][ny] = 0

    x, y = nx, ny
    # 이동할 때마다 주사위 윗 면 출력
    print(dice[0])  # d1 = dice[0]
