from collections import deque
#n, k = 5, 17 # 수빈이가 있는 위치, 동생이 있는 위치
n, k = map(int, input().split())
MAX = 10 ** 5
visited = [0]*(MAX+1)
# 걷기 : 1초 후 x-1, x+1로이동
# 순간이동 : 1초 후 2*x 으로 이동
# 가장 빠른 시간 찾기

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()

        if x == k:
            print(visited[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not visited[nx]:
                visited[nx] = visited[x] + 1
                queue.append(nx)

bfs()
