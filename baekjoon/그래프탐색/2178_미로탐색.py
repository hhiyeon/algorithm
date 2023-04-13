from collections import deque

n, m = map(int, input().split())  # 가로, 세로
board = [list(map(int, input())) for _ in range(n)]


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        node_x, node_y = queue.popleft()

        for d in range(4):
            next_x = node_x + dx[d]
            next_y = node_y + dy[d]

            # 다음 노드가 그래프 밖으로 벗어 나지 않고, 이동 가능 한지(1) 확인
            if 0 <= next_x < n and 0 <= next_y < m and board[next_x][next_y] == 1:
                queue.append([next_x, next_y])  # 이동 가능한 노드 큐 삽입
                board[next_x][next_y] = board[node_x][node_y] + 1  # 현재 이동한 거리 + 1 갱신
    return board[n - 1][m - 1]  # 도착지 cost 반환


print(bfs(0, 0))
