from collections import defaultdict


def classifier(k, tangerine):
    cnt_size = defaultdict(int)
    cnt_result = 0

    for t in tangerine:
        cnt_size[t] += 1

    # value 내림차순 정렬
    sorted_cnt = sorted(cnt_size.items(), key=lambda x: x[1], reverse=True)

    for key, value in sorted_cnt:
        k -= value
        cnt_result += 1
        if k <= 0:
            break
    return cnt_result

def solution(k, tangerine):
    answer = classifier(k, tangerine)
    print(answer)
    return answer


solution(4, [1, 3, 2, 5, 4, 5, 2, 3])
