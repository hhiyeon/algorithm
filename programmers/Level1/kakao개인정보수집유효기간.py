# 소요시간 1시간
from collections import defaultdict


def get_period(year, month, day, num_option):
    cal_year = num_option // 12
    year += cal_year
    month = month + num_option - cal_year * 12

    if day == 1:  # day 가 첫째 일수면 이전 달로
        day = 28
        month -= 1
    else:
        day -= 1
    if month > 12:  # month 가 12월이 넘어가면 다음 연도로
        while month > 12:
            year += 1
            month -= 12
    return [year, month, day]


def cal_period(today, terms, privacies):
    array_result = []
    dict_option = defaultdict(int)

    for x in terms:
        terms_type = x[0]
        period = int(x[2:])
        dict_option[terms_type] = period

    for idx in range(len(privacies)):
        year, month, day = int(privacies[idx][:4]), int(privacies[idx][5:7]), int(privacies[idx][8:10])
        expiration = get_period(year, month, day, dict_option[privacies[idx][-1]])

        t_year, t_month, t_day = map(int, today.split("."))
        # y, m, d = today.split('.')

        if t_year > expiration[0]:  # 연도가 더 적은 경우
            array_result.append(idx + 1)
            continue
        elif t_year == expiration[0] and t_month > expiration[1]:  # 달이 더 적은 경우
            array_result.append(idx + 1)
            continue
        elif t_year == expiration[0] and t_month == expiration[1] and t_day > expiration[2]:
            array_result.append(idx + 1)
            continue
    return array_result


def solution(today, terms, privacies):
    answer = cal_period(today, terms, privacies);
    print(answer)
    return answer
