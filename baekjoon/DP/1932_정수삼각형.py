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

# dp[1][1] = arr[1][1]
# dp[2][1] = dp[1][1] + arr[2][1]
# dp[2][2] = dp[1][1] + arr[2][2]
# dp[3][1] = dp[2][1] + arr[3][1]
# dp[3][2] = max(dp[2][1] + arr[3][2], dp[2][2] + arr[3][3])
# dp[3][3] = dp[2][2] + arr[3][3]
