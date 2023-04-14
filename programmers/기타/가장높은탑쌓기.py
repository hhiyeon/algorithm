def solution(n, arr):
    # output 10
    bricks = []
    for i in range(n):
        s, h, w = arr[i][0], arr[i][1], arr[i][2]
        bricks.append((s,h,w)) # 벽돌 정보

    bricks.sort(reverse=True) # 넓이를 내림차순으로 정렬
    dp = [0]*n
    dp[0] = bricks[0][1] # 벽돌의 높이
    res = bricks[0][1]
    for i in range(1, n):
        max_h = 0
        for j in range(i-1, -1, -1):
            if bricks[j][2]>bricks[i][2] and dp[j] > max_h:
                max_h = dp[j]
        dp[i] = max_h+bricks[i][1]
        res = max(res, dp[i])
    return res

n = 5
arr = [[25, 3, 4], [4, 4, 6], [9, 2, 3], [16, 2, 5], [1, 5, 2]]
# 넓이, 높이, 무게 순서
# 벽돌의 넓이가 큰 순서부터 쌓아준다 -> 25, 16, 9, 4, 1
# 무게만 고려해서 dp
print(solution(n, arr))
