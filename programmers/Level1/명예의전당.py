# 프로그램 시작 ~ k일까지 점수 계산
# 명예의 전당 점수 개수 K
# 명예의 전당 최하위 점수 출력

def min_score(k, score):
    rank_list = []
    result_list = []

    for num in score:
        if len(rank_list) < k:  # 명예의 전당이 비어있는 경우
            rank_list.append(num)
        else:
            min_rank = min(rank_list)
            if min_rank < num:  # 명예의 전당 점수가 더 낮은 경우
                rank_list.remove(min_rank)
                rank_list.append(num)
        result_list.append(min(rank_list))

    return result_list


def solution():
    min_score(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])


solution()
