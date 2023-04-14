def solution(clothes):
    answer = 1
    dict = {}

    for i in range(len(clothes)):
        opt = clothes[i][1]
        wear = clothes[i][0]
        dict.setdefault(opt, 0)
        dict[opt] += 1

    for key in dict.keys():
        answer = answer * (dict[key] + 1)
    answer -= 1
    return answer