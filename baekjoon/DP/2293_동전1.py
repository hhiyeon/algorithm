#n, k = map(int, input().split())
#coins = []
#for _ in range(n):
#    coins.append(int(input()))
n, k = 3, 10
coins = [1, 2, 5]

dp = [0] * (k + 1)
dp[0] = 1

# coin원의 동전으로 i원을 만들기
# coin원으로 동전 만드는 경우의수 = dp[i-coin]
for coin in coins:
    for i in range(coin, k+1):
        dp[i] = dp[i] + dp[i-coin]

print(dp)
print(dp[k])
