# import re
# from collections import Counter
#
# S = input()
#
# S = re.sub("0+", "0", S)
# S = re.sub("1+", "1", S)
#
# cnt_value = Counter(S)
# print(min(cnt_value["0"], cnt_value["1"]))

S = input()
a_cnt = 1
b_cnt = 0
check_type = S[0]
check_flag = True

for idx in range(1, len(S)):
    if check_type != S[idx]:
        if check_flag:
            b_cnt += 1
            check_flag = False
        else:
            a_cnt += 1  # 첫 번째랑 같은 값
            check_flag = True
        check_type = S[idx]

print(min(a_cnt, b_cnt))
