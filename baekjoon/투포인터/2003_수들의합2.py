import sys

N, M = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))

lt = 0
rt = 1
cnt = 0  # 경우의 수

while N >= rt >= lt:
    total = sum(n_list[lt:rt])
    if total == M:  # 일치 하면 cnt
        cnt += 1
        rt += 1
    elif total > M:  # 값이 크면
        lt += 1
    else:
        rt += 1
print(cnt)
