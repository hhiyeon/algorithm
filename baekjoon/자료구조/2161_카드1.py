from collections import deque

n = int(input())

# 1장 남을 때 까지 반복
# 제일 위의 카드를 바닥에 버린다
# 제일 위에 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
queue = deque()
answer = []

for i in range(n):
    queue.append(n - i)

while len(queue) != 0:
    answer.append(queue.pop())
    if len(queue) != 0:
        queue.appendleft(queue.pop())

print(*answer)
