n = int(input())  # 집 개수
R = [0] * (n + 1)
G = [0] * (n + 1)
B = [0] * (n + 1)
dp = [[0 for col in range(3)] for row in range(n + 1)]
for i in range(1, n + 1):
    color = list(input().split())
    R[i] = int(color[0])
    G[i] = int(color[1])
    B[i] = int(color[2])

if n == 1:
    print(min(R[1], G[1], B[1]))

else:
    # 초기값 설정
    dp[1][0] = R[1]
    dp[1][1] = G[1]
    dp[1][2] = B[1]
    # 집 색칠 규칙
    # 1. 1번의 집 색상은 2번의 집 색상과 같지 않아야 한다.
    # 2. N번 집의 색상은 N-1번의 집 색상과 같지 않아야 한다.
    # 3. 2(<= i <= N-1)번의 집 색상은 i-1번, i+1번 집의 색상과 같지 않아야 한다.

    for k in range(2, n + 1):
        dp[k][0] = min(dp[k - 1][1], dp[k - 1][2]) + R[k] # 이전색상 초록 or 파랑 + 현재 빨강
        dp[k][1] = min(dp[k - 1][0], dp[k - 1][2]) + G[k] # 이전색상 파랑 or 빨강 + 현재 초록
        dp[k][2] = min(dp[k - 1][0], dp[k - 1][1]) + B[k] # 이전색상 빨강 or 파랑 + 현재 파랑

print(min(dp[n][0], dp[n][1], dp[n][2]))
