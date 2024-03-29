import sys

input = sys.stdin.readline
n = int(input())
dp = [0] * (n + 1)
schedule = [list(map(int, input().split())) for _ in range(n)]

for i in range(n - 1, -1, -1):
    if i + schedule[i][0] > n:  # 상담일 > 퇴사일 넘기지 않기
        dp[i] = dp[i + 1]
    else:  # 상담을 하지 않을 때, 오늘 보수 + 오늘 진행한 상담 시간 이후로 넘어간 날 보수
        dp[i] = max(dp[i + 1], schedule[i][1] + dp[i + schedule[i][0]])

print(dp[0])
