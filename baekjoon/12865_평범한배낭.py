#n, k = 4, 7 # 물품의 수, 버틸 수 있는 무게
#info = [[0,0],[6,13],[4,8],[3,6],[5,12]] # 무게, 가치
n, k = map(int, input().split())
info = [[0,0]]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)] # 총 무게, 총 가치

for _ in range(n):
    w, v = map(int, input().split()) # 무게, 가치
    info.append([w,v])

for i in range(1, n+1):
    for j in range(1, k+1):
        w, v = info[i][0], info[i][1] # 무게, 가치

        if j < w: # 무게가 남았을 때
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])
    #print(dp)
print(dp[n][k])
