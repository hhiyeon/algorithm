import math


def solution(progresses, speeds):
    # 작업의 진도, 작업의 개발 속도
    answer = []
    arr = []
    front = 0

    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        day = math.ceil(remain / speeds[i])
        arr.append(day)

    for idx in range(len(arr)):
        if arr[idx] > arr[front]:  # 더 큰 수가 나오면
            print(idx, front)
            answer.append(idx - front)
            front = idx
    answer.append(len(arr) - front)

    return answer