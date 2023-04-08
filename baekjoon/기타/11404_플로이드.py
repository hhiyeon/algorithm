#n = 5 # 도시의 개수
#m = 14 # 버스의 개수
n = int(input())
m = int(input())
inf = float('inf')
dp = [[inf for _ in range(n+1)] for _ in range(n+1)] # 최소 비용 테이블
# 버스의 정보 : 시작 도시 a, 도착 도시 b, 필요 비용 c
for _ in range(m):
    a, b, c = map(int, input().split())
    dp[a][b] = min(c, dp[a][b])

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j: # 자기 자신은 X
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

for x in range(1, n+1):
    for y in range(1, n+1):
        if dp[x][y] == inf:
            print(0, end=' ')
        else:
            print(dp[x][y], end=' ')
    print()