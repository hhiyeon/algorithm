s1 = input()
s2 = input()
s3 = input()

l1 = len(s1)
l2 = len(s2)
l3 = len(s3)

# 문자열 3개 LCS 구하기
dp = [[[0] * (l3 + 1) for _ in range(l2 + 1)] for _ in range(l1 + 1)]

for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        for z in range(1, l3 + 1):
            if s1[i - 1] == s2[j - 1] == s3[z - 1]:
                dp[i][j][z] = dp[i - 1][j - 1][z - 1] + 1
            else:  # 같지 않은 경우, 이전 값들 중에 제일 큰 값으로
                dp[i][j][z] = max(dp[i - 1][j][z], dp[i][j - 1][z], dp[i][j][z - 1])

print(dp[l1][l2][l3])  # 마지막 값 = 최장 길이
