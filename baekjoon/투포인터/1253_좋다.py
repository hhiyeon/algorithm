import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

num_list.sort()
cnt = 0

for idx in range(N):
    value = num_list[idx]
    check_list = num_list[:idx] + num_list[idx+1:]
    lt = 0
    rt = len(check_list) - 1

    while lt < rt:
        lt_num = check_list[lt]
        rt_num = check_list[rt]
        total = lt_num + rt_num
        if total == value:  # 값이 있으면
            cnt += 1
            break

        if value < total:  # 더 크면
            rt -= 1
        else:
            lt += 1

print(cnt)

# 2, 0 0 -> 0