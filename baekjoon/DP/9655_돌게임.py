n = int(input())

# 돌 1개 또는 3개

dp = [0] * 1001
dp[1] = 1  # 1(상근)
dp[2] = 0  # 1 1(창영)
dp[3] = 1  # 1 1 1(상근)

for i in range(4, n + 1):
    if dp[i - 1] or dp[i - 3]:  # 돌이 3개가 남거나 1개가 남으면 승패가 결정됨
        dp[i] = 0  # 창영
    else:
        dp[i] = 1  # 상근

if dp[n]:
    print('SK')
else:
    print('CY')
