#n, m = map(int, input().split())
#arr = list(map(int, input().split()))
#n, m = 4, 4
#arr = [1,1,2,2]
n, m = 4,2
arr = [999,1,23,5]
#arr = [9,7,9,1]
arr = sorted(arr) # 오름차순
stack = []

def dfs(v):
    if len(stack) == m:
        print(stack)
        return

    prev = 0
    for x in range(v, n):
        if prev != arr[x]:
            stack.append(arr[x])
            prev = arr[x]
            dfs(x+1)
            stack.pop()
dfs(0)
