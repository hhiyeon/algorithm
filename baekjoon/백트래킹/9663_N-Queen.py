def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


def dfs(x):
    global result

    if x == n:
        result += 1
        return
    for i in range(n):
        if visite[i]:
            continue
        row[x] = i
        if adjacent(x):
            visite[i] = True
            dfs(x + 1)
            visite[i] = False

import sys

# n = int(sys.stdin.readline())
n = 8  # n x n 크기의 체스판
row = [0] * n
visite = [False] * n
result = 0
dfs(0)
print(result)
