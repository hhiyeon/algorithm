#n, m = map(int, input().split())
#arr = list(map(int, input().split()))
n, m = 4, 2
arr = [9,7,9,1]
arr = sorted(arr)
stack =[]

def dfs(v):
    if len(stack) == m:
        print(*stack)
        return
    prev = 0
    for x in range(v, n):
        if prev != arr[x]:
            stack.append(arr[x])
            prev = arr[x]
            dfs(x)
            stack.pop()
dfs(0)
