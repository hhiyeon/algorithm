from collections import deque
#n, m = 3, 2 # 학생의 번호 1~n, m는 키를 비교환 횟수
n, m = map(int, input().split())
inDegree = [0]*(n+1)
graph = [[] for i in range(n+1)]
queue = deque()
answer = []
arr = []
# 1 -> 3
# 2 -> 3

# 키를 비교한 두 학생의 번호 a,b (학생 a가 b앞에)
# 그래프에 정점끼리 연결된 정보들 입력
for _ in range(m):
    a, b = map(int, input().split())
    arr.append([a,b])

for a, b in arr:
    inDegree[b] += 1
    graph[a].append(b)

for i in range(1, n+1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    top = queue.popleft() # 큐 최상위 정점
    for b in graph[top]:
        inDegree[b] -= 1
        if inDegree[b] == 0:
            queue.append(b)
    answer.append(top)

print(*answer)