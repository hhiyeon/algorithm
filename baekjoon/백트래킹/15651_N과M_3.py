# n, m = map(int, input().split())
n, m = 4,2 
stack = []

def dfs():
    if m == len(stack):
        print(' '.join(map(str, stack)))
        return
    for x in range(1, n+1):
        stack.append(x)
        dfs()
        stack.pop()
dfs()
