from collections import deque
#n = 6 # 카드 개수, 1~n번
n = int(input())
queue = deque()

for i in range(1,n+1):
    queue.append(i)

while True:
    if len(queue) == 1:
        break

    # 맨 위 버리기
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])