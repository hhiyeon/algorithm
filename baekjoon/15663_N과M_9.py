#n, m = map(int, input().split())
#arr = list(map(int, input().split()))

n, m = 4, 2
arr = [9,7,9,1]
arr = sorted(arr)
visited = [False]*n # 사용한 원소 체크
stack = []
answer = []

def dfs(v):
    if len(stack) == m:
        answer.append(tuple(stack))
        return
    
    for x in range(0, n):
        if visited[x]:
            continue
        stack.append(arr[x])
        visited[x] = True # 사용
        dfs(v+1)
        visited[x] = False # 사용끝
        stack.pop() 
dfs(0)

# 오름차순, set 중복제거
for x in sorted(list(set(answer))):
    print(*x) # 튜플 출력
