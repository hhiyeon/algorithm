# 문자열 s가 주어질 때 각 문자들의 가장 가까운 글자를 출력
# 처음이면 -1 출력
# 딕셔너리로 마지막 위치를 나타내기
from collections import defaultdict


def make_result(s):
    str_result = []
    dict_location = defaultdict(int)

    for index in range(len(s)):
        key = s[index]
        if key not in dict_location:  # 처음인 경우
            str_result.append(-1)
        else:  # 위치 정보가 있는 경우
            distance = index - dict_location[key]
            str_result.append(distance)
        dict_location[key] = index  # 위치 갱신
    return str_result


def solution():
    print(make_result("banana"))


solution()
