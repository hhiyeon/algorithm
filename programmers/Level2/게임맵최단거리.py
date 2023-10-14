from collections import deque


def solution(maps):
    answer = 0

    # 상대 팀 진영에 빨리 도착 하는 칸 최소값 or 도착 못하는 경우 -1
    # 동서남북 한 칸씩, (1,1)에서 시작 (n,m) 도착
    # 벽 있는 자리 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n, m = len(maps), len(maps[0])

    def bfs(x, y):
        queue = deque()
        queue.append([x, y])

        while queue:
            cx, cy = queue.popleft()  # 현재 노드

            if [cx, cy] == [n - 1, m - 1]:  # 도착지 확인
                return maps[cx][cy]

            for d in range(4):  # 다음 노드
                nx = cx + dx[d]
                ny = cy + dy[d]

                # 범위에서 벗어나지 않고, 벽 없는 곳
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[cx][cy] + 1
                    queue.append([nx, ny])  # 다음 노드 입력

        return -1

    return bfs(0, 0)


test1 = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
print(solution(test1))  # 11
