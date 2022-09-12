#n, m = map(int, input().split())
#arr = list(map(int, input().split()))

n, m = 4, 2
arr = [9,8,7,1]
arr = sorted(arr)
stack = []

def dfs(start):
    if len(stack) == m:
        for idx in stack:
            print(arr[idx], end=' ')
        print()
        return
    
    for x in range(start, n):
        stack.append(x)
        dfs(x)
        stack.pop()
dfs(0)
