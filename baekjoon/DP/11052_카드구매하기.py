n = int(input())  # 카드 개수
array = [0] + list(map(int, input().split()))  # 카드 가격
# n = 4
# array = [0, 1, 5, 6, 7]
dp = [0] * (n + 1)
dp[0] = 0
dp[1] = array[0]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + array[j])

print(dp[n])
