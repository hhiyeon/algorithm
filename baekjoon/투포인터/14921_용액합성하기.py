import sys

N = int(sys.stdin.readline())  # 용액의 수
a_list = list(map(int, sys.stdin.readline().split()))  # 용액 특성 값
# 두 용액 섞어서 특성 값이 0에 가까운 용액 만들기

lt = 0
rt = N - 1
value = a_list[lt] + a_list[rt]

while lt < rt:
    total = a_list[lt] + a_list[rt]

    if total == 0:
        value = 0
        break

    if abs(total) < abs(value):  # 용액의 크기가 작을 때
        value = total

    if total < 0:  # 용액이 작으면
        lt += 1
    else:  # 용액 크기가 클떄
        rt -= 1

print(value)
