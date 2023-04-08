# N x M 미로에서 (1,1) 에서 (N,M)으로 이동하기
# (r+1, c), (r, c+1), (r+1, c+1) 으로 이동 가능
# 가져올 수 있는 사탕의 최대 값
n, m = map(int, input().split())
board = []
dp = [[0] *(m+1) for _ in range(n+1)]
for i in range(n):
    board.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = board[i-1][j-1] + max(dp[i][j-1], dp[i-1][j], dp[i][j])

print(dp[n][m])