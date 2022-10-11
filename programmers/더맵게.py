from heapq import *


def solution(scoville, K):  # 음식의 스코빌지수, 원하는 스코빌 지수 -> 섞는 최소 횟수 구하기
    answer = 0
    heapify(scoville)

    while scoville[0] < K:
        num1 = heappop(scoville)
        num2 = heappop(scoville)
        heappush(scoville, num1 + num2 * 2)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return answer