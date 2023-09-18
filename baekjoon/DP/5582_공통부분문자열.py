n1 = str(input().rstrip())
n2 = str(input().rstrip())

dp = [[0] * (len(n2) + 1) for _ in range(len(n1) + 1)]
answer = 0

for i in range(1, len(n1) + 1):
    for j in range(1, len(n2) + 1):
        if n1[i - 1] == n2[j - 1]:  # 공통 문자열
            dp[i][j] = dp[i - 1][j - 1] + 1
            answer = max(answer, dp[i][j])
print(answer)
