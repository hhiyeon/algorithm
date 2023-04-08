#line1 = 'ACAYKP'
#line2 = 'CAPCAK'
import sys
line1 = sys.stdin.readline().strip().upper()
line2 = sys.stdin.readline().strip().upper()
n1 = len(line1)
n2 = len(line2)
dp = [[0]*(n2+1) for _ in range(n1+1)]

for i in range(1, n1+1):
    for j in range(1, n2+1):
        if line1[i-1] == line2[j-1]: # 문자가 같은 경우
            dp[i][j] = dp[i-1][j-1] + 1 # 글자 추가전에 가장 큰 길이 + 1
        else: # 글자가 서로 다르면
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) # 이전에 있던 문자들 중에서 가장 큰 값
print(dp[-1][-1])