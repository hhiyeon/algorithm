n = int(input())
arr = list(map(int, input().split()))
s = []
maxValue = 0

def dfs():
    global maxValue
    if len(s) == n:
        total = 0
        for x in range(1, n):
            total += abs(arr[s[x-1]] - arr[s[x]])
        maxValue = max(maxValue, total)
    else:
        for idx in range(n):
            if idx not in s:
                s.append(idx)
                dfs()
                s.pop()

dfs()
print(maxValue)
