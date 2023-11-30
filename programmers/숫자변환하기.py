from collections import deque
def solution(x, y, n):
    answer = 0
    queue = deque()

    def bfs(count, x, cal):
        while queue:
            value = queue.pop()
            if value * n or value * 2 or value * 3:
                return

            x = x

    answer = bfs(0, x, 0)

    return answer


x = 10
y = 40
n = 5
print(solution(x, y, n))
