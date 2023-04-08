# coding=utf-8
# n = 5  # 숫자 카드 개수
# cNum = [6, 3, 2, 10, -10]  # 숫자 카드 번호
# m = 8  # 확인 숫자 개수
# card = [10, 9, -5, 2, 3, 4, 5, -10]  # 확인할 번호(있으면 1, 없으면 0)
import sys
import sys
n = int(input())
cNum = list(map(int, sys.stdin.readline().split()))
m = int(input())
card = list(map(int, sys.stdin.readline().split()))
cNum = sorted(cNum)
answer = ''
#print(cNum)
for num in card:
    lt = 0
    rt = n - 1
    flag = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        if cNum[mid] < num:
            lt = mid +1
        elif cNum[mid] == num:
            flag = 1
            break
        else:
            # cNum[lt] > num
            rt = mid -1
    answer += str(flag) + ' '
print(answer[:-1])

