def check_word(s):
    first_word = s[0]
    cnt1 = 1
    cnt2 = 0

    for idx in range(1, len(s)):
        word = s[idx]
        if word != first_word:
            cnt2 += 1
        else:
            cnt1 += 1
        if cnt1 == cnt2:
            s = s[idx + 1:]
            break
    return s


def cnt_result(s):
    del_cnt = 0
    while s:
        if len(s) == 1:
            del_cnt += 1
            return del_cnt
        if len(s) == 0:
            break
        after_s = check_word(s)
        if len(after_s) == len(s):
            del_cnt += 1
            break
        del_cnt += 1
        s = after_s
    return del_cnt


def solution(s):
    answer = cnt_result(s)
    print(answer)
    return answer


solution("baaa")
