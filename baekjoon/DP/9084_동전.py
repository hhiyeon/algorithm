t = int(input())  # 테스트 케이스

for _ in range(t):
    n = int(input())  # 동전 종류
    coins = list(map(int, input().split()))  # 동전 금액
    m = int(input())  # 구해야 하는 값
    dp = [0] * (m + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, m + 1):  # 각 동전마다 개수 구하기
            dp[i] += dp[i - coin]
    print(dp[m])
