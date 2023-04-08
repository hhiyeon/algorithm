import sys
n, m = map(int, sys.stdin.readline().split()) # 수의 개수, 합을 구해야하는 횟수
arr = list(map(int, sys.stdin.readline().split()))
dp = [0]*(n+1)
# D[i] = A[1] + A[2] + .. + A[i]
# D[i] = D[i-1] + A[i]
for i in range(1, n+1):
    dp[i] = dp[i-1] + arr[i-1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(dp[j]-dp[i-1])