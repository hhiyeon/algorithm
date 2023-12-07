import sys

n = int(sys.stdin.readline())
dp = [0] * 31

# 0, 1 일때는 채울 수 있는 경우 X
dp[2] = 3  # 세로 3개, 세로 2개 + 가로 1개
# 3: 다 못채움
# 4: 2일 때 3가지씩 + 위 아래 2개

for i in range(4, n + 1):
    if i % 2 == 0:
        dp[i] = dp[i - 2] * 3 + sum(dp[:i - 2]) * 2 + 2

print(dp[n])
