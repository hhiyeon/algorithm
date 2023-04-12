import sys

N = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))

lt = 0
rt = N - 1
ans = n_list[lt] + n_list[rt]
ans_list = [lt, rt]

while lt < rt:
    total = n_list[lt] + n_list[rt]
    # print(total)

    if abs(ans) > abs(total):
        ans = total
        ans_list = [lt, rt]

    if total == 0:
        break
    elif total < 0:
        lt += 1
    else:
        rt -= 1

print(n_list[ans_list[0]], n_list[ans_list[1]])
