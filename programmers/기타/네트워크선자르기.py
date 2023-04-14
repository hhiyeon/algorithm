def solution(n):
    answer = 0
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2

    for k in range(3, n + 1):
        dp[k] = dp[k - 2] + dp[k - 1]

    answer = dp[n]
    return answer

print(solution(7))

# 1 1 1 + 1
# 2 1 + 1
# 1 2 + 1
# 1 1 + 2
# 2 + 2
# 3만드는방법 + 1 D[3]
# 2만드는방법 + 2 D[2]
# D[i] = D[2] + D[3]
# D[4] = D[k-2] + D[k-1]

# def DFS(len):
#     global dy
#     if dy[len] > 0:  # 값이 있으면 메모이제이션
#         return dy[len]
#     if len == 1 or len == 2:
#         return len
#     else:
#         dy[len] = DFS(len - 1) + DFS(len - 2)
#         return dy[len]
#
# def solution(n):
#     answer = 0
#     n = int(input())
#     dy = [0] * (n + 1)
#     answer = DFS(n)
#     return answer
#
# print(solution(7))