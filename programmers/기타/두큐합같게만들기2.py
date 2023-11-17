from collections import deque


def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)

    while True:
        if sum1 == sum2:
            break
        # print(sum1, sum2, q1, q2)

        if sum1 < sum2:  # 오른 쪽이 더 큰 경우
            value = q2.popleft()
            q1.append(value)
            sum1 += value
            sum2 -= value
        elif sum1 > sum2:  # 왼쪽이 더 큰 경우
            value = q1.popleft()
            q2.append(value)
            sum1 -= value
            sum2 += value

        answer += 1

        if answer > len(queue1) * 4:  # 전체 배열의 길이 2n -> 최대 이동 4n
            answer = -1
            break
        # print(answer)

    return answer


q1 = [1, 1]
q2 = [1, 5]

print(solution(q1, q2))
