# 빵 1, 야채 2, 고기 3
# 1 -> 2 -> 3 -> 1

def cnt_burger(ingredient):
    cnt = 0
    stack = []

    for idx in ingredient:
        stack.append(idx)
        if [1, 2, 3, 1] == stack[-4:]:
            cnt += 1
            for _ in range(4):
                stack.pop()
    return cnt


def solution(ingredient):
    answer = cnt_burger(ingredient)
    return answer


solution([2, 1, 1, 2, 3, 1, 2, 3, 1, 1, 2, 3, 1, 2])