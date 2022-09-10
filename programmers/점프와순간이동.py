def solution(n):
    ans = 0
    
    # 1. K칸 앞으로 점프 - k 건전지 소요
    # 2. (현재까지 온 거리) * 2 순간이동 - 건전지 소요 X
    
    while True:
        if n % 2 == 0:
            n //= 2
        else:
            ans += 1
            n -= 1
        if n == 0:
            break

    return ans
