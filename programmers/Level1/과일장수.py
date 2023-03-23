# 사과 상태 1점 ~ k점
# 가장 낮은 상태의 점수 p점 / 사과 개수 m개 씩 포장
# 사과 한 상자 가격 p * m

# 내림차순 배열 만들어서 스택 방법으로 제거
from collections import deque


def score_result(k, m, score):
    total_score = 0

    # 내림차순 정렬
    deque_score = deque(sorted(score, reverse=True))

    while len(deque_score) >= m:
        min_score = float("inf")  # 양의 무한대
        for _ in range(m):
            min_score = min(deque_score.popleft(), min_score)  # deque 앞에 원소 제거
        price_box = min_score * m
        total_score += price_box

    return total_score


def solution():
    answer = score_result(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])
    return answer


solution()
