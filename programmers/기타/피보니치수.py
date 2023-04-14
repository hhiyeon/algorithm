def solution(n):
    if n == 1 or n == 0:
        return 1
    answer = 0
    start = 0
    fibo = 1

    for i in range(2, n + 1):
        answer = (start + fibo) % 1234567
        start = fibo
        fibo = answer
    return answer