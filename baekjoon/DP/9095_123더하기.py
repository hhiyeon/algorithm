tc = int(input())
# 1. 테이블 정의하기
# 2. 점화식
# 3. 초기값

# dp[n] = 1, 2, 3합으로 나타내는 방법의 수

# dp[4] = ?
# (1+1+1) (3) (2+1), (1+2) // 3을 1,2,3으로 나타내는 방법 : 3 구하고 + 1 = 4
# (1+1), (2) // 2를 1,2,3으로 나타내는 방법 : 2 구하고 + 2 = 4
# (1) // 1을 1,2,3으로 나타내는 방법 : 1 구하고 + 3 = 4
# DP[4] = D[1] + D[2] + D[3] -> dp[n] = dp[n-3] + dp[n-2] + dp[n-1]

for _ in range(tc):
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        dp = [0] * (n + 1)
        dp[1], dp[2], dp[3] = 1, 2, 4
        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        print(dp[n])
