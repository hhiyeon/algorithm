n, k = 3, 15 # 경우의 수 말고 동전 개수 구하기
coins = [1, 5, 12]
dp = [float('inf')] * (k+1)
dp[0] = 0
for coin in coins:
    for i in range(coin, k+1): # 각 동전마다 개수 구하기
        dp[i] = min(dp[i], dp[i-coin] + 1)
    print(dp)
if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])
# n = 1
# 1
#
# n = 2
# 1 1
#
# n = 3
# 1 1 1(2만든거 +1)
#
# n = 4
# 1 1 1 1(3만든거 +1)
#
# n = 5
# 5
#
# n = 6
# 5 1