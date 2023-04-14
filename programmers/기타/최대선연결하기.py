def solution(n, arr):
    # output 6
    answer = 0
    arr.insert(0,0)
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        max = 0
        for j in range(i-1, 0, -1):
            if arr[i] > arr[j] and dp[j] > max:
                max = dp[j]
        dp[i] = max + 1
        if dp[i] > answer:
            answer = dp[i]
    return answer

n = 10
arr = [4, 1, 2, 3, 9, 7, 5, 6, 10, 8]
print(solution(n, arr))