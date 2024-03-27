import sys

n = int(sys.stdin.readline())
rgb = [list(map(int, input().split())) for _ in range(n)]
answer = I = 1e9

for i in range(3):
    dp = [[I, I, I] for _ in range(n)]
    dp[0][i] = rgb[0][i]
    for j in range(1, n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + rgb[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + rgb[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + rgb[j][2]
    for k in range(3):
        if i != k:
            answer = min(answer, dp[-1][k])
print(answer)
