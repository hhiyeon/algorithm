# n 숫자 카드 개수
# m 구해야 하는 숫자 카드 개수
# n = 10
# cArr1 = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
# m = 8
# cArr2 = [10, 9, -5, 2, 3, 4, 5, -10]
from collections import defaultdict
import sys
n = int(sys.stdin.readline())
cArr1 = list(map(int,sys.stdin.readline().split()))
m = sys.stdin.readline()
cArr2 = list(map(int,sys.stdin.readline().split()))
dict = defaultdict(int)

for x in cArr1:
    dict[x] = dict.get(x, 0) + 1
res = ''
for element in cArr2:
    if element in dict:
        print(dict[element], end=' ')
    else:
        print(0, end=' ')

