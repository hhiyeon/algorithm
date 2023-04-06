# 일정 금액 지불 시 10일 동안 회원 자격
# 회원 대상으로 매일 한가지 제품 할인 - 하루에 하나 구매

from collections import defaultdict


def get_result(want, number, discount):
    day_cnt = 0
    max_day = len(discount) - 9

    for idx in range(max_day):
        sale_list = discount[idx:idx + 10]
        dict_item = defaultdict(int)
        for item in sale_list:
            dict_item[item] += 1

        non_product = True

        for product in range(len(want)):
            if dict_item[want[product]] < number[product]:
                non_product = False
                break

        if non_product:
            day_cnt += 1

    return day_cnt


def solution(want, number, discount):
    answer = get_result(want, number, discount)
    return answer


want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana",
            "apple", "banana"]

solution(want, number, discount)
