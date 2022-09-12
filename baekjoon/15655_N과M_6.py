#n, m = map(int, input().split())
#arr = list(map(int, input().split()))
n, m = 4, 4
arr = [1231, 1232, 1233, 1234]
arr = sorted(arr)
stack = []

def dfs(start):
    if len(stack) == m:
        for idx in stack:
            print(arr[idx], end=' ')
        print()
        return
    for x in range(start, n):
        if x not in stack:
            stack.append(x)
            dfs(x+1)
            stack.pop()
dfs(0)
