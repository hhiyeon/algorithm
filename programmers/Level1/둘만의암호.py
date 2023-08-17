def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for ch in s:
        idx = alpha.index(ch) + 1
        a_list = []

        while len(a_list) < index:
            if alpha[idx % 26] not in list(skip):
                a_list.append(alpha[idx % 26])
            idx = idx + 1
        answer += a_list[-1]
    return answer