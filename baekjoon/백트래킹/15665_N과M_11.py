n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)
stack = []

def dfs():
    if len(stack) == m:
        print(*stack)
        return
    prev = 0
    for x in range(0, n):
        if prev != arr[x]:
            stack.append(arr[x])
            prev = arr[x]
            dfs()
            stack.pop()
dfs()
