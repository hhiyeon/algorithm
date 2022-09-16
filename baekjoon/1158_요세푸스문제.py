from collections import deque
# n, k = 7, 3 # 사람 수, 제거하는 사람 위치
n, k = map(int,input().split())
queue = deque() # 덱으로 큐 생성
answer = '<'

# 요소 삽입
for x in range(1, n+1):
    queue.append(x)

while queue:
    for x in range(k-1):
        element = queue.popleft() # 맨 왼쪽에 있는 값 꺼내서
        queue.append(element) # 맨 뒤로 삽입
    answer += str(queue.popleft()) + ', '

print(answer[:-2]+'>')

