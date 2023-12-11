import sys

n = int(sys.stdin.readline())

dp = [0] * 1001
dp[1] = 1
dp[2] = 3  # 2x1 2개, 1x2 2개, 2x2 1개

for i in range(3, n + 1):
    dp[i] = (dp[i - 2] * 2) + dp[i - 1]  # i-2 모양 앞뒤로 2가지 경우 + i-1 모양 그대로 1개

print(dp[n] % 10007)
