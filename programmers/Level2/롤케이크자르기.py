from collections import Counter


def solution(topping):
    answer = 0
    count = Counter(topping)
    set1 = set()

    for num in topping:
        count[num] -= 1
        set1.add(num)

        if count[num] == 0:
            count.pop(num)

        if len(count) == len(set1):
            answer += 1
        # print(count, set1, answer)

    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
