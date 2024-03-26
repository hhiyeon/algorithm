import sys

n = int(sys.stdin.readline())

dp = []

for i in range(n):
    dp.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:  # 맨 왼쪽
            dp[i][j] += dp[i - 1][0]
        elif j == i:  # 맨 오른쪽
            dp[i][j] += dp[i - 1][j - 1]
        else:  # 최대값 구하기
            dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])
# print(dp)
print(max(dp[n-1]))
