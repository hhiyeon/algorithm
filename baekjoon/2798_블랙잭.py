n, m = map(int, input().split())
arr = list(map(int, input().split()))
maxValue = 0
stack = []

def dfs():
    global maxValue
    if len(stack) == 3:
        total = 0
        for value in stack:
            total += arr[value]
        if maxValue < total and total <= m:
            maxValue = total
    else:
        for idx in range(n):
            if idx not in stack:
                stack.append(idx)
                dfs()
                stack.pop()

dfs()
print(maxValue)
