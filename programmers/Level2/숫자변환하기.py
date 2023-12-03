from collections import deque


def solution(x, y, n):
    queue = deque([(x, 0)])  # 현재 값, 연산 횟수
    visited = set()

    while queue:
        cur, count = queue.popleft()
        if cur == y:  # 결과가 나온 경우 연산 횟수 출력
            return count

        def type_operate(next_value):
            if next_value <= y and next_value not in visited:
                queue.append((next_value, count + 1))
                visited.add(next_value)

        type_operate(cur + n)
        type_operate(cur * 2)
        type_operate(cur * 3)

    return -1


x = 10
y = 40
n = 5
print(solution(x, y, n))
