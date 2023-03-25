# X와 Y의 공통 정수로 가장 큰 정수 만들기
from collections import defaultdict


def get_dict_cnt(str_num):
    dict = defaultdict(int)
    for x in range(len(str_num)):
        number = int(str_num[x])
        dict[number] += 1
    return dict


def pair_number(X, Y):
    max_num = ''
    dict_X = get_dict_cnt(X)
    dict_Y = get_dict_cnt(Y)

    reversed_Y = sorted(dict_Y.items(), reverse=True)
    print(dict_X, reversed_Y)

    for key, value in reversed_Y:
        if key not in dict_X:
            continue
        if key == 0:
            if len(max_num) == 0:
                max_num = "0"
                break
            else:
                max_num += str(key)*min(value, dict_X[key])
        else:
            max_num += str(key)*min(value, dict_X[key])
        print(max_num)
    return max_num

def solution():
    result = pair_number("100", "100")
    print("-1" if len(result) == 0 else result)
    return "-1" if len(result) == 0 else result


solution()
