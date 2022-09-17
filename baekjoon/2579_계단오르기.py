n = int(input()) # 계단의 개수
S = [0]*(n+1)
for i in range(1, n+1):
    S[i] = int(input())

if n == 1:
    print(S[1])
elif n == 2:
    print(S[1]+S[2])
else:
    dp = [[0 for col in range(3)] for row in range(n+1)]
    dp[1][1], dp[1][2] = S[1], 0
    dp[2][1], dp[2][2] = S[2], S[1]+S[2]
    # 계단 오르기 규칙
    # 1. 한 계단 또는 두 계단 오르기 가능
    # 2. 연속 세개 계단 불가능(시작점은 포함X)
    # 3. 마지막 계단 무조건 밟기

    for i in range(3,n+1):
        dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + S[i]
        dp[i][2] = dp[i-1][1] + S[i]

    print(max(dp[n][1], dp[n][2]))