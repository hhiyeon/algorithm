# 원형 수열의 연속 부분으로 부분 수열의 합으로 만들 수 있는 개수 구하기


def get_cnt(elements):
    sum_list = set()
    max_size = len(elements)
    elements = elements * 2

    for i in range(max_size):
        for j in range(max_size):
            sum_list.add(sum(elements[j:j + i + 1]))

    return len(sum_list)


def solution(elements):
    answer = get_cnt(elements)
    return answer


solution([7, 9, 1, 1, 4])
