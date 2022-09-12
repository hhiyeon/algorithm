n, m = map(int, input().split())
arr = list(map(int, input().split()))
#n, m = 4, 2
#arr = [9,8,7,1]
arr = sorted(arr) # 사전순 출력
stack = []

def dfs(start):
    if len(stack) == m:
        for idx in stack:
            print(arr[idx], end=' ')
        print()
        return

    for x in range(0, n):
        # 중복 상관 X
        stack.append(x)
        dfs(start+1)
        stack.pop()

dfs(0)
