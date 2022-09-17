import sys
n = int(sys.stdin.readline())
dp = [0]*(n+1)
answer = [0]*(n+1)
res = ''
dp[1] = 0

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    answer[i] = i-1

    if (i % 3 == 0) and (dp[i] > dp[i//3]+1): # 1번
        dp[i] = dp[i//3]+1
        answer[i] = i // 3
    elif (i % 2 == 0) and (dp[i] > dp[i//2]+1): # 2번
        dp[i] = dp[i//2]+1
        answer[i] = i // 2

print(dp[n])
current = n

while True:
    res += str(current) + ' '
    if current == 1:
        break
    current = answer[current]

print(res[:-1])