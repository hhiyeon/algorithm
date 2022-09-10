def solution(n, left, right):
    answer = []

    # 위치값//n, i%n 중에 큰 값에 +1 하면 해당 위치의 값을 구할 수 있다.
    for i in range(left, right + 1):
        answer.append(max(i//n, i%n) + 1)
    return answer
