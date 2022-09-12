n, m = map(int, input().split())
stack = []

def dfs(start):
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
    else:
        for x in range(start, n+1):
            if x not in stack:
                stack.append(x)
                #print(stack)
                dfs(x+1)
                stack.pop()
dfs(1)

