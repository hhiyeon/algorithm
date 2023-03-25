# 6 -2 = 4
# 4 / m-1 반올림 = result
#
# 4 -1 = 3

from collections import deque

def get_fill_cnt(n, m, section):
    dq_section = deque(section)
    del_cnt = 0
    if m == 1:  # 1칸씩 칠해야 하는 경우
        return len(section)

    while dq_section:
        del_cnt += 1
        top_element = dq_section[0]
        del_element = top_element + m

        while dq_section[0] < del_element:
            dq_section.popleft()
            if len(dq_section) == 0:
                break

    return del_cnt


def solution():
    answer = get_fill_cnt(16, 4, [2, 3, 15, 16])
    # answer = get_fill_cnt(8,2,[2,4])
    # answer = get_fill_cnt(8,4,[2,3,6])
    print(answer)


solution()
