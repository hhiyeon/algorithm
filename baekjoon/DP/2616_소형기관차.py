import sys

n = int(sys.stdin.readline())
arrays = list(map(int, sys.stdin.readline().split()))
max_train = int(sys.stdin.readline())

S = [0]
value = 0
for items in arrays:
    value += items
    S.append(value)

dp = [[0] * (n + 1) for _ in range(4)]

for i in range(1, 4):
    for j in range(i * max_train, n + 1):
        if i == 1:
            dp[i][j] = max(dp[i][j - 1], S[j] - S[j - max_train])
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - max_train] + S[j] - S[j - max_train])

print(dp[3][n])
